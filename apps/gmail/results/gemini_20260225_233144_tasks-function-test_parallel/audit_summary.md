# Audit Report: Gmail Function Test — Gemini 20260225_233144

**Overall**: 24/50 passed (48%) — 26 failures analyzed below.

## Sanity Check Result

All 50 verifier sanity checks **PASS** — verifiers are correct when state is properly set.

---

## Part 1: UI/Code Bugs Found (8 bugs, blocking 14+ tasks)

### Bug 1: Label picker `data-label-id` mismatch
- **Location**: `js/app.js:361` reads `labelPickerItem.dataset.labelId` from the `<label>` wrapper, but `data-label-id` is on the nested `<input>` checkbox (`js/views.js:1090`)
- **Effect**: `labelId` is always `undefined`, so labels are **never applied or removed** through the label picker
- **Fix**: `labelPickerItem.dataset.labelId` → `checkbox.dataset.labelId`
- **Blocks**: task_m12, task_h8, task_h14 (directly); task_h10, task_h11, task_h12, task_h13 (label step of multi-step)

### Bug 2: No "Delete forever" for individual emails in Spam/Trash
- **Location**: `js/app.js:1076-1085` — `delete-email` handler always calls `trashEmails()`, never `deleteForever()` even when already in trash/spam. Delete forever only exposed in trash list view "More" menu, not in spam and not in email detail view.
- **Fix**: Check `isTrashed`/`isSpam` and call `deleteForever()` instead
- **Blocks**: task_e5, task_e15

### Bug 3: Theme selector UI not rendered
- **Location**: `js/views.js` — no theme dropdown or radio group rendered anywhere in Settings despite handler code existing in `js/app.js:830` and state support for `settings.theme`
- **Fix**: Add theme selector to `_renderSettingsGeneral()`
- **Blocks**: task_m15

### Bug 4: No category move options in "Move to" dialog
- **Location**: `js/views.js:766` — `showMoveToPicker()` filters out `CATEGORY_*` labels; `move-to-category` handler exists in `app.js:1008` but is unreachable from UI
- **Fix**: Add Primary/Social/Promotions/Updates/Forums options to "Move to" picker
- **Blocks**: task_m10, task_h11

### Bug 5: Discard draft doesn't remove email from state
- **Location**: `js/app.js:667-670` — `discard-draft` handler only calls `closeCompose()` and shows a toast, never removes the draft email from `AppState.emails`
- **Fix**: Delete the draft email from state before closing
- **Blocks**: task_m11

### Bug 6: Filter category action hardcoded to `null`
- **Location**: `js/app.js:1842` — `category: null` hardcoded; the `filterActionCategory` dropdown value is never read during save
- **Fix**: `category: document.getElementById('filterActionCategory')?.value || null`
- **Secondary**: task_m8 verifier (`task_m8.py:20`) also crashes on `None.lower()` — should guard against null
- **Blocks**: task_m8

### Bug 7: No unsnooze UI
- **Location**: `unsnoozeEmails()` exists in `js/state.js:427` but only called as undo action after snooze (`js/app.js:1330`). No button/menu in snoozed view or email detail.
- **Fix**: Add unsnooze action in snoozed email view (context menu or toolbar button)
- **Blocks**: task_m19

### Bug 8: Create label parent ID mismatch
- **Location**: `js/views.js:1260` renders dropdown with id `labelParentDropdown`, but `js/app.js:1690` reads `document.getElementById('labelParentSelect')` — ID doesn't exist, so `parentId` is always null for new labels
- **Note**: Edit label dialog works correctly (uses raw `<select id="labelParentSelect">` at `app.js:1716`)
- **Fix**: Change `app.js:1690` to read from `labelParentDropdown`
- **Blocks**: task_h5

---

## Part 2: Task-by-Task Classification

### Failures caused by UI bugs (14 tasks — would pass if bugs are fixed)

| Task | Difficulty | Bug # | Details |
|------|-----------|-------|---------|
| task_e5 | easy | #2 | Delete from spam moves to trash instead of permanent delete |
| task_e15 | easy | #2 | Delete from trash re-trashes instead of permanent delete |
| task_m8 | medium | #6 | Filter category action hardcoded to null + verifier null crash |
| task_m10 | medium | #4 | No category options in Move To picker |
| task_m11 | medium | #5 | Discard draft only closes modal, doesn't delete |
| task_m12 | medium | #1 | Label picker data-label-id read from wrong element |
| task_m15 | medium | #3 | Theme selector UI doesn't exist |
| task_m19 | medium | #7 | No unsnooze button/menu |
| task_h5 | hard | #8 | Create label reads parentId from wrong element ID |
| task_h8 | hard | #1 | Label picker broken — can't apply labels |
| task_h11 | hard | #4,#1 | Category move UI missing + label picker broken |
| task_h12 | hard | #1 | Label picker broken — can't remove labels |
| task_h13 | hard | #1 | Label picker broken — Health label not applied |
| task_h14 | hard | #1 | Label picker broken — can't apply to 3 emails |

### Failures caused by agent (12 tasks — no benchmark changes needed)

| Task | Difficulty | Agent Issue |
|------|-----------|-------------|
| task_e3 | easy | Block sender exists in Settings → Blocked Senders; agent claimed success but didn't actually add to blockedSenders |
| task_e6 | easy | Mute exists in right-click context menu; agent created a filter instead |
| task_e7 | easy | Archived email visible in All Mail; agent couldn't find it |
| task_e11 | easy | Button labels setting renders in Settings → General; agent said it couldn't locate it |
| task_m1 | medium | Label color editing works via Settings → Labels → edit; agent claimed success but color unchanged |
| task_m3 | medium | Category toggles work in Settings → Inbox; agent claimed success but Forums still enabled |
| task_m5 | medium | Visibility toggle works in Settings → Labels; agent claimed success but visible=true |
| task_m9 | medium | Star + important both work in UI; agent failed on isImportant |
| task_m18 | medium | Reply behavior setting exists in Settings → General; agent claimed success but unchanged |
| task_h7 | hard | Multiple Inboxes section editing works; agent claimed success but query unchanged |
| task_h9 | hard | 3/4 settings changed; importance markers toggle exists in Settings → Inbox but agent missed it |
| task_h10 | hard | Star works in UI but isStarred=False; label would also fail due to Bug #1 but star failure is agent's fault |

---

## Part 3: Summary

| Category | Count |
|----------|-------|
| Passed | 24 |
| Failed — UI bug | 14 |
| Failed — Agent | 12 |
| **Total** | **50** |

- **Current pass rate**: 48% (24/50)
- **Estimated pass rate after bug fixes**: up to **76%** (38/50) — the 14 bug-blocked tasks become passable
- **Agent-attributable pass rate** (fair benchmark): 24/36 = **67%** on non-buggy tasks

### Priority fixes (by task count blocked)

1. **Bug #1** (label picker) — blocks 7 tasks, single-line fix
2. **Bug #2** (delete forever) — blocks 2 tasks
3. **Bug #4** (category move) — blocks 2 tasks
4. Bugs #3, #5, #6, #7, #8 — block 1 task each
