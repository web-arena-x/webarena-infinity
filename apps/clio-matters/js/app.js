/* app.js — Router, event delegation, and lifecycle for Clio Matters */
/* eslint-disable */

const App = {
    _sidebarCollapsed: false,
    _openDropdowns: new Set(),
    _formData: {},
    _sortableState: null,
    _damageFilter: 'all',
    _expandedProviderSections: {},
    _expandedPracticeAreas: new Set(),
    _collapsedFormSections: new Set(),
    _confirmCallback: null,
    _toastCounter: 0,

    // ========================================================================
    // Initialization
    // ========================================================================

    init() {
        AppState.init();
        AppState.subscribe(() => this.render());
        this._setupEventListeners();
        this._setupHashRouter();
        this._parseRoute();
        this.render();
    },

    // ========================================================================
    // Routing (hash-based)
    // ========================================================================

    _setupHashRouter() {
        window.addEventListener('hashchange', () => {
            this._parseRoute();
            this.render();
        });
    },

    _parseRoute() {
        const hash = window.location.hash || '#/matters';
        const parts = hash.slice(2).split('/');

        if (parts[0] === 'matters') {
            if (parts[1] === 'new') {
                AppState.currentView = 'matter-form';
                AppState.currentMatterId = null;
                this._formData = this._getDefaultFormData();
            } else if (parts[1] && parts[2] === 'edit') {
                AppState.currentView = 'matter-form';
                AppState.currentMatterId = parts[1];
                this._formData = this._getMatterFormData(parts[1]);
            } else if (parts[1] && parts[2] === 'damages') {
                AppState.currentView = 'matter-dashboard';
                AppState.currentMatterId = parts[1];
                AppState.currentSubTab = 'damages';
            } else if (parts[1] && parts[2] === 'medical-records') {
                AppState.currentView = 'matter-dashboard';
                AppState.currentMatterId = parts[1];
                AppState.currentSubTab = 'medical-records';
            } else if (parts[1] && parts[2] === 'settlement') {
                AppState.currentView = 'matter-dashboard';
                AppState.currentMatterId = parts[1];
                AppState.currentSubTab = 'settlement';
            } else if (parts[1]) {
                AppState.currentView = 'matter-dashboard';
                AppState.currentMatterId = parts[1];
                if (!AppState.currentSubTab) AppState.currentSubTab = 'overview';
            } else {
                AppState.currentView = 'matters-list';
                AppState.currentMatterId = null;
            }
        } else if (parts[0] === 'stages') {
            AppState.currentView = 'stages';
        } else if (parts[0] === 'settings') {
            AppState.currentView = 'settings';
            if (parts[1]) AppState.settingsTab = parts[1];
        } else if (parts[0] === 'recovery-bin') {
            AppState.currentView = 'recovery-bin';
        } else {
            AppState.currentView = 'matters-list';
        }
    },

    // ========================================================================
    // Rendering
    // ========================================================================

    render() {
        const sidebar = document.getElementById('sidebar');
        const mainContent = document.getElementById('mainContent');

        if (sidebar) {
            sidebar.innerHTML = Views.renderSidebar();
            sidebar.classList.toggle('collapsed', this._sidebarCollapsed);
        }

        if (mainContent) {
            let content = '';
            switch (AppState.currentView) {
                case 'matters-list':
                    content = Views.renderMattersListView();
                    break;
                case 'matter-form':
                    content = Views.renderMatterFormView(AppState.currentMatterId);
                    break;
                case 'matter-dashboard':
                    content = Views.renderMatterDashboardView(AppState.currentMatterId);
                    break;
                case 'stages':
                    content = Views.renderStagesView();
                    break;
                case 'settings':
                    content = Views.renderSettingsView();
                    break;
                case 'recovery-bin':
                    content = Views.renderRecoveryBinView();
                    break;
                default:
                    content = Views.renderMattersListView();
            }
            mainContent.innerHTML = content;
        }

        // Render modal if open
        const modalOverlay = document.getElementById('modalOverlay');
        if (modalOverlay) {
            if (AppState.modalData) {
                modalOverlay.classList.add('open');
                document.getElementById('modalTitle').innerHTML = AppState.modalData.title || '';
                document.getElementById('modalBody').innerHTML = AppState.modalData.body || '';
                document.getElementById('modalFooter').innerHTML = AppState.modalData.footer || '';
            } else {
                modalOverlay.classList.remove('open');
            }
        }

        // Restore dropdown open states after re-render
        this._openDropdowns.forEach(id => {
            const menu = document.getElementById(`${id}-menu`);
            if (menu) menu.classList.add('open');
            const trigger = document.querySelector(`[data-dropdown-trigger="${id}"]`);
            if (trigger) trigger.classList.add('open');
        });
    },

    // ========================================================================
    // Event Handling (delegation pattern)
    // ========================================================================

    _setupEventListeners() {
        // Click delegation
        document.addEventListener('click', (e) => {
            const target = e.target.closest('[data-action]') ||
                           e.target.closest('[data-route]') ||
                           e.target.closest('[data-dropdown-trigger]') ||
                           e.target.closest('[data-dropdown-item]') ||
                           e.target.closest('[data-multi-item]') ||
                           e.target.closest('[data-checkbox]') ||
                           e.target.closest('[data-toggle]');

            // Close dropdowns on outside click
            if (!e.target.closest('.custom-dropdown')) {
                this._closeAllDropdowns();
            }

            if (!target) return;

            // Handle routes
            if (target.dataset.route !== undefined) {
                e.preventDefault();
                window.location.hash = target.dataset.route;
                return;
            }

            // Handle dropdown triggers
            if (target.dataset.dropdownTrigger !== undefined) {
                e.preventDefault();
                this._toggleDropdown(target.dataset.dropdownTrigger);
                return;
            }

            // Handle dropdown item selection
            if (target.dataset.dropdownItem !== undefined) {
                e.preventDefault();
                this._handleDropdownSelect(target.dataset.dropdownItem, target.dataset.value);
                return;
            }

            // Handle multi-select dropdown items
            if (target.dataset.multiItem !== undefined) {
                e.preventDefault();
                this._handleMultiDropdownSelect(target.dataset.multiItem, target.dataset.value);
                return;
            }

            // Handle checkboxes
            if (target.dataset.checkbox !== undefined) {
                this._handleCheckbox(target.dataset.checkbox);
                return;
            }

            // Handle toggles
            if (target.dataset.toggle !== undefined) {
                this._handleToggle(target.dataset.toggle);
                return;
            }

            // Handle actions
            if (target.dataset.action !== undefined) {
                this._handleAction(target.dataset.action, target);
                return;
            }
        });

        // Input delegation (for search, form fields)
        document.addEventListener('input', (e) => {
            if (e.target.id === 'matters-search') {
                AppState.setSearchQuery(e.target.value);
            }
            if (e.target.dataset.dropdownSearch !== undefined) {
                this._handleDropdownSearch(e.target.dataset.dropdownSearch, e.target.value);
            }
            // Form field changes
            if (e.target.dataset.formField !== undefined) {
                this._formData[e.target.dataset.formField] = e.target.value;
            }
            // Medical search
            if (e.target.id === 'medical-search' || e.target.dataset.action === 'medical-search-input') {
                App._medicalSearchQuery = e.target.value;
                // debounce or direct re-render
                this.render();
            }
        });

        // Keydown for dropdown navigation and modal escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this._closeAllDropdowns();
                if (AppState.modalData) {
                    AppState.modalData = null;
                    this.render();
                }
            }
        });
    },

    // ========================================================================
    // Action Handler (main dispatch)
    // ========================================================================

    _handleAction(action, target) {
        switch (action) {
            // ---- Sidebar ----
            case 'toggle-sidebar':
                this._sidebarCollapsed = !this._sidebarCollapsed;
                this.render();
                break;

            // ---- Matter list actions ----
            case 'set-status-filter':
                AppState.setStatusFilter(target.dataset.status);
                break;
            case 'search-input':
                // handled in input event
                break;
            case 'clear-search':
                AppState.setSearchQuery('');
                break;
            case 'select-all':
                this._handleSelectAll();
                break;
            case 'select-row':
                this._handleSelectRow(target.dataset.id);
                break;
            case 'sort':
                this._handleSort(target.dataset.sortField);
                break;
            case 'prev-page':
                AppState.setPage(AppState.currentPage - 1);
                break;
            case 'next-page':
                AppState.setPage(AppState.currentPage + 1);
                break;
            case 'goto-page':
                AppState.setPage(parseInt(target.dataset.page));
                break;
            case 'export-csv':
                this._exportMattersCSV();
                break;

            // ---- Bulk actions ----
            case 'bulk-close':
                AppState.bulkUpdateStatus(AppState.selectedMatterIds, 'closed');
                AppState.selectedMatterIds = [];
                this._showToast('Matters closed successfully', 'success');
                break;
            case 'bulk-delete':
                this._showConfirmModal('Delete Matters',
                    `Are you sure you want to delete ${AppState.selectedMatterIds.length} matter(s)? They can be recovered from the Recovery Bin.`,
                    () => {
                        AppState.bulkDeleteMatters(AppState.selectedMatterIds);
                        AppState.selectedMatterIds = [];
                        this._showToast('Matters deleted', 'success');
                    });
                break;
            case 'bulk-update-status':
                this._showStatusPickerModal();
                break;

            // ---- Filter actions ----
            case 'set-filter':
                AppState.setFilter(target.dataset.filterKey, target.dataset.filterValue);
                break;
            case 'remove-filter':
                AppState.setFilter(target.dataset.filterKey, null);
                break;
            case 'clear-filters':
                AppState.clearFilters();
                break;

            // ---- Matter form actions ----
            case 'save-matter':
                this._saveMatter();
                break;
            case 'save-and-conflict-check':
                this._saveMatter();
                this._showToast('Conflict check initiated', 'info');
                break;
            case 'cancel-form':
                window.history.back();
                break;
            case 'delete-matter':
                this._showConfirmModal('Delete Matter',
                    'Are you sure you want to delete this matter? It can be recovered from the Recovery Bin.',
                    () => {
                        AppState.deleteMatter(AppState.currentMatterId);
                        window.location.hash = '#/matters';
                        this._showToast('Matter deleted', 'success');
                    });
                break;
            case 'apply-template':
                this._applyTemplate();
                break;
            case 'add-related-contact':
                this._addRelatedContact();
                break;
            case 'remove-related-contact':
                this._removeRelatedContact(parseInt(target.dataset.index));
                break;
            case 'add-document-folder':
                this._addDocumentFolder();
                break;
            case 'remove-document-folder':
                this._removeDocumentFolder(parseInt(target.dataset.index));
                break;
            case 'add-notification-recipient':
                this._addNotificationRecipient();
                break;
            case 'remove-notification-recipient':
                this._removeNotificationRecipient(parseInt(target.dataset.index));
                break;

            // ---- Form section toggle ----
            case 'toggle-section':
                this._toggleFormSection(target.dataset.section);
                break;

            // ---- Matter dashboard actions ----
            case 'change-matter-status': {
                const matterId = target.dataset.id;
                const newStatus = target.dataset.status;
                if (newStatus === 'closed') {
                    AppState.closeMatter(matterId);
                } else if (newStatus === 'open') {
                    AppState.reopenMatter(matterId);
                } else {
                    AppState.updateMatter(matterId, { status: newStatus });
                }
                this._showToast(`Matter status changed to ${newStatus}`, 'success');
                break;
            }
            case 'change-sub-tab':
                AppState.currentSubTab = target.dataset.tab;
                if (AppState.currentMatterId) {
                    const tabMap = { 'overview': '', 'damages': '/damages', 'medical-records': '/medical-records', 'settlement': '/settlement' };
                    window.location.hash = '#/matters/' + AppState.currentMatterId + (tabMap[target.dataset.tab] || '');
                } else {
                    this.render();
                }
                break;
            case 'duplicate-matter': {
                const newMatter = AppState.duplicateMatter(target.dataset.id);
                if (newMatter) {
                    window.location.hash = `#/matters/${newMatter.id}`;
                    this._showToast('Matter duplicated', 'success');
                }
                break;
            }
            case 'edit-matter-inline':
                window.location.hash = `#/matters/${target.dataset.id}/edit`;
                break;

            // ---- Damages actions ----
            case 'add-damage':
                this._showDamageFormModal();
                break;
            case 'edit-damage':
                this._showDamageFormModal(target.dataset.id);
                break;
            case 'delete-damage':
                this._showConfirmModal('Delete Damage',
                    'Are you sure you want to delete this damage? This action cannot be undone.',
                    () => {
                        AppState.deleteDamage(target.dataset.id);
                        this._showToast('Damage deleted', 'success');
                    });
                break;
            case 'save-damage':
                this._saveDamage();
                break;
            case 'filter-damages':
                this._damageFilter = target.dataset.type || 'all';
                this.render();
                break;

            // ---- Medical Records actions ----
            case 'add-provider':
                this._showProviderFormModal();
                break;
            case 'edit-provider':
                this._showProviderFormModal(target.dataset.id);
                break;
            case 'delete-provider':
                this._showConfirmModal('Delete Medical Provider',
                    'This will also delete all associated records and bills. Continue?',
                    () => {
                        AppState.deleteMedicalProvider(target.dataset.id);
                        this._showToast('Provider deleted', 'success');
                    });
                break;
            case 'save-provider':
                this._saveMedicalProvider();
                break;
            case 'toggle-provider-records':
                this._toggleProviderSection(target.dataset.id, 'records');
                break;
            case 'toggle-provider-bills':
                this._toggleProviderSection(target.dataset.id, 'bills');
                break;

            // ---- Settlement actions ----
            case 'add-recovery':
                this._showRecoveryFormModal();
                break;
            case 'edit-recovery':
                this._showRecoveryFormModal(target.dataset.id);
                break;
            case 'delete-recovery':
                this._showConfirmModal('Delete Recovery',
                    'Are you sure?',
                    () => {
                        AppState.deleteRecovery(AppState.currentMatterId, target.dataset.id);
                        this._showToast('Recovery deleted', 'success');
                    });
                break;
            case 'save-recovery':
                this._saveRecovery();
                break;
            case 'add-legal-fee':
                this._showLegalFeeFormModal();
                break;
            case 'edit-legal-fee':
                this._showLegalFeeFormModal(target.dataset.id);
                break;
            case 'delete-legal-fee':
                AppState.deleteLegalFee(AppState.currentMatterId, target.dataset.id);
                this._showToast('Legal fee deleted', 'success');
                break;
            case 'save-legal-fee':
                this._saveLegalFee();
                break;
            case 'add-lien':
                this._showLienFormModal();
                break;
            case 'edit-lien':
                this._showLienFormModal(target.dataset.id);
                break;
            case 'delete-lien':
                AppState.deleteNonMedicalLien(AppState.currentMatterId, target.dataset.id);
                this._showToast('Lien deleted', 'success');
                break;
            case 'save-lien':
                this._saveLien();
                break;
            case 'add-outstanding-balance':
                this._showOutstandingBalanceFormModal();
                break;
            case 'edit-outstanding-balance':
                this._showOutstandingBalanceFormModal(target.dataset.id);
                break;
            case 'delete-outstanding-balance':
                AppState.deleteOutstandingBalance(AppState.currentMatterId, target.dataset.id);
                this._showToast('Balance deleted', 'success');
                break;
            case 'save-outstanding-balance':
                this._saveOutstandingBalance();
                break;
            case 'change-deduction-order': {
                const settlement = AppState.getSettlement(AppState.currentMatterId);
                settlement.deductionOrder = target.dataset.value;
                AppState.notify();
                this._showToast('Deduction order updated', 'success');
                break;
            }

            // ---- Kanban/Stages actions ----
            case 'select-practice-area':
                AppState.stagesSelectedPracticeAreaId = target.dataset.id;
                this.render();
                break;
            case 'move-matter-stage':
                AppState.moveMatterToStage(target.dataset.matterId, target.dataset.stageId);
                this._showToast('Matter moved', 'success');
                break;
            case 'kanban-close-matter':
                AppState.closeMatter(target.dataset.id);
                this._showToast('Matter closed', 'success');
                break;
            case 'kanban-toggle-status': {
                const matter = AppState.getMatterById(target.dataset.id);
                if (matter) {
                    const newStatus = matter.status === 'open' ? 'pending' : 'open';
                    AppState.updateMatter(target.dataset.id, { status: newStatus });
                    this._showToast(`Matter marked as ${newStatus}`, 'success');
                }
                break;
            }

            // ---- Settings actions ----
            case 'settings-tab':
                AppState.settingsTab = target.dataset.tab;
                window.location.hash = `#/settings/${target.dataset.tab}`;
                break;
            case 'add-practice-area':
                this._showPracticeAreaFormModal();
                break;
            case 'edit-practice-area':
                this._showPracticeAreaFormModal(target.dataset.id);
                break;
            case 'delete-practice-area':
                this._deletePracticeArea(target.dataset.id);
                break;
            case 'save-practice-area':
                this._savePracticeArea();
                break;
            case 'add-stage':
                this._showStageFormModal(target.dataset.practiceAreaId);
                break;
            case 'edit-stage':
                this._showStageFormModal(target.dataset.practiceAreaId, target.dataset.stageId);
                break;
            case 'delete-stage':
                AppState.deleteStage(target.dataset.practiceAreaId, target.dataset.stageId);
                this._showToast('Stage deleted', 'success');
                break;
            case 'save-stage':
                this._saveStage();
                break;
            case 'toggle-practice-area-stages':
                this._togglePracticeAreaStages(target.dataset.id);
                break;
            case 'create-template':
                this._showTemplateFormModal();
                break;
            case 'edit-template':
                this._showTemplateFormModal(target.dataset.id);
                break;
            case 'delete-template':
                this._showConfirmModal('Delete Template', 'Delete this template?', () => {
                    AppState.deleteTemplate(target.dataset.id);
                    this._showToast('Template deleted', 'success');
                });
                break;
            case 'set-default-template':
                AppState.setDefaultTemplate(target.dataset.id);
                this._showToast('Default template updated', 'success');
                break;
            case 'save-template':
                this._saveTemplate();
                break;
            case 'save-numbering':
                this._saveNumberingScheme();
                break;
            case 'save-notifications':
                this._saveNotificationSettings();
                break;

            // ---- Recovery bin ----
            case 'recover-matter':
                AppState.recoverMatter(target.dataset.id);
                this._showToast('Matter recovered', 'success');
                break;

            // ---- Modal actions ----
            case 'close-modal':
                AppState.modalData = null;
                this._confirmCallback = null;
                this.render();
                break;
            case 'confirm-modal':
                if (this._confirmCallback) {
                    this._confirmCallback();
                    this._confirmCallback = null;
                }
                AppState.modalData = null;
                this.render();
                break;

            // ---- Toast ----
            case 'close-toast':
                document.getElementById(target.dataset.toastId)?.remove();
                break;

            // ---- Kanban menu actions ----
            case 'show-kanban-menu': {
                const menuEl = document.getElementById('kanban-menu-' + target.dataset.id);
                if (menuEl) menuEl.classList.toggle('open');
                break;
            }
            case 'kanban-mark-pending': {
                AppState.updateMatter(target.dataset.id, { status: 'pending' });
                this._showToast('Matter marked as pending', 'success');
                break;
            }
            case 'kanban-mark-open': {
                AppState.updateMatter(target.dataset.id, { status: 'open' });
                this._showToast('Matter marked as open', 'success');
                break;
            }
            case 'kanban-switch-pa':
                // Show practice area selection - simplified toast for now
                this._showToast('Switch practice area feature', 'info');
                break;

            // ---- Related contact form actions ----
            case 'show-add-related-contact': {
                const form = document.getElementById('add-related-contact-form');
                if (form) form.style.display = form.style.display === 'none' ? 'block' : 'none';
                break;
            }
            case 'save-related-contact':
                this._addRelatedContact();
                break;
            case 'cancel-related-contact': {
                const rcForm = document.getElementById('add-related-contact-form');
                if (rcForm) rcForm.style.display = 'none';
                break;
            }

            // ---- Expand/collapse sections ----
            case 'toggle-expand': {
                const expandId = target.dataset.id || target.dataset.providerId;
                const section = target.dataset.section;
                this._toggleProviderSection(expandId, section);
                break;
            }

            // ---- Quick actions ----
            case 'quick-bill':
                this._showToast('Quick bill generated', 'info');
                break;
            case 'add-time-entry':
                this._showToast('Time entry feature coming soon', 'info');
                break;
            case 'add-expense':
                this._showToast('Expense feature coming soon', 'info');
                break;
            case 'view-contact':
                // Navigate to contact detail (not implemented - show toast)
                this._showToast('Contact details view', 'info');
                break;
            case 'view-all-activity':
                this._showToast('Full activity log view', 'info');
                break;
            case 'email-contact':
                // No-op for testing (would open mailto: in real app)
                break;
            case 'copy-address': {
                const address = target.dataset.address || target.closest('[data-address]')?.dataset.address || '';
                if (address && navigator.clipboard) {
                    navigator.clipboard.writeText(address);
                    this._showToast('Address copied', 'success');
                }
                break;
            }
            case 'generate-settlement-statement':
                this._showToast('Settlement statement generated', 'success');
                break;

            // ---- Modal overlay actions ----
            case 'close-modal-overlay':
                AppState.modalData = null;
                this.render();
                break;
            case 'submit-modal-form':
                // Delegate to the appropriate save handler based on modal type
                if (AppState.modalData && AppState.modalData.saveAction) {
                    this._handleAction(AppState.modalData.saveAction, target);
                }
                break;

            // ---- Medical search actions ----
            case 'medical-search-input':
                // Handled in input event listener
                break;
            case 'clear-medical-search':
                App._medicalSearchQuery = '';
                this.render();
                break;

            // ---- Tag actions ----
            case 'remove-tag':
                // Generic tag removal - handled by specific parent context
                break;
        }
    },

    // ========================================================================
    // Dropdown Management
    // ========================================================================

    _toggleDropdown(id) {
        if (this._openDropdowns.has(id)) {
            this._openDropdowns.delete(id);
            const menu = document.getElementById(`${id}-menu`);
            if (menu) menu.classList.remove('open');
            const trigger = document.querySelector(`[data-dropdown-trigger="${id}"]`);
            if (trigger) trigger.classList.remove('open');
        } else {
            // Close all others first
            this._closeAllDropdowns();
            this._openDropdowns.add(id);
            const menu = document.getElementById(`${id}-menu`);
            if (menu) menu.classList.add('open');
            const trigger = document.querySelector(`[data-dropdown-trigger="${id}"]`);
            if (trigger) trigger.classList.add('open');
        }
    },

    _closeAllDropdowns() {
        this._openDropdowns.forEach(id => {
            const menu = document.getElementById(`${id}-menu`);
            if (menu) menu.classList.remove('open');
            const trigger = document.querySelector(`[data-dropdown-trigger="${id}"]`);
            if (trigger) trigger.classList.remove('open');
        });
        this._openDropdowns.clear();
    },

    _handleDropdownSelect(id, value) {
        this._closeAllDropdowns();

        // Parse value to integer if it looks like a number (for IDs)
        const numValue = /^\d+$/.test(value) ? parseInt(value) : value;

        // Map dropdown IDs to state changes
        if (id === 'filter-practice-area') {
            AppState.setFilter('practiceAreaId', numValue || null);
        } else if (id === 'filter-responsible-attorney') {
            AppState.setFilter('responsibleAttorneyId', numValue || null);
        } else if (id === 'filter-originating-attorney') {
            AppState.setFilter('originatingAttorneyId', numValue || null);
        } else if (id === 'filter-billing-method') {
            AppState.setFilter('billingMethod', value || null);
        } else if (id === 'stages-practice-area') {
            AppState.stagesSelectedPracticeAreaId = numValue;
            this.render();
        } else if (id === 'dashboard-status') {
            const matterId = AppState.currentMatterId;
            if (value === 'closed') { AppState.closeMatter(matterId); }
            else if (value === 'open') { AppState.reopenMatter(matterId); }
            else { AppState.updateMatter(matterId, { status: value }); }
            this._showToast('Status changed to ' + value, 'success');
        } else if (id.startsWith('status-change-')) {
            const matterId = id.replace('status-change-', '');
            if (value === 'closed') {
                AppState.closeMatter(matterId);
            } else if (value === 'open') {
                AppState.reopenMatter(matterId);
            } else {
                AppState.updateMatter(matterId, { status: value });
            }
            this._showToast(`Matter status changed to ${value}`, 'success');
        } else if (id === 'bulk-status-picker') {
            // Bulk status update from modal
            AppState.bulkUpdateStatus(AppState.selectedMatterIds, value);
            AppState.selectedMatterIds = [];
            AppState.modalData = null;
            this._showToast(`Matters updated to ${value}`, 'success');
            this.render();
        } else if (id === 'move-stage') {
            // Move matter to stage from dropdown
            const parts = value.split(':');
            if (parts.length === 2) {
                AppState.moveMatterToStage(parts[0], parts[1]);
                this._showToast('Matter moved', 'success');
            }
        } else if (id === 'filter-treatment-status' || id === 'filter-record-status' || id === 'filter-bill-status') {
            if (!App._medicalFilters) App._medicalFilters = {};
            App._medicalFilters[id.replace('filter-', '')] = value === '' ? null : value;
            this.render();
        } else if (id === 'medical-sort') {
            App._medicalSort = value;
            this.render();
        } else if (id.startsWith('form-')) {
            // Form field dropdowns: form-{fieldName}
            const field = id.replace('form-', '');
            this._formData[field] = numValue;
            this.render();
        } else if (id.startsWith('modal-')) {
            // Modal form field dropdowns: modal-{fieldName}
            const field = id.replace('modal-', '');
            this._formData['modal_' + field] = value === '' ? '' : numValue;
            // Re-render modal body to show selected value
            this._rerenderModalDropdowns(id, value);
        } else {
            // Generic fallback: store in _formData
            this._formData[id] = numValue;
            this.render();
        }
    },

    _handleMultiDropdownSelect(id, value) {
        const numValue = /^\d+$/.test(value) ? parseInt(value) : value;

        if (id.startsWith('form-')) {
            const field = id.replace('form-', '');
            if (!Array.isArray(this._formData[field])) {
                this._formData[field] = [];
            }
            const idx = this._formData[field].indexOf(numValue);
            if (idx === -1) {
                this._formData[field].push(numValue);
            } else {
                this._formData[field].splice(idx, 1);
            }
            this.render();
        } else if (id.startsWith('modal-')) {
            const field = 'modal_' + id.replace('modal-', '');
            if (!Array.isArray(this._formData[field])) {
                this._formData[field] = [];
            }
            const idx = this._formData[field].indexOf(numValue);
            if (idx === -1) {
                this._formData[field].push(numValue);
            } else {
                this._formData[field].splice(idx, 1);
            }
        }
    },

    _handleDropdownSearch(id, query) {
        const dropdown = document.getElementById(`${id}-dropdown`);
        if (!dropdown) return;
        const options = dropdown.querySelectorAll('.dropdown-item');
        const q = query.toLowerCase();
        options.forEach(opt => {
            const text = opt.textContent.toLowerCase();
            opt.style.display = text.includes(q) ? '' : 'none';
        });
    },

    _rerenderModalDropdowns(id, value) {
        // Update the dropdown trigger text to reflect the selected value
        const dropdown = document.getElementById(`${id}-dropdown`);
        if (!dropdown) return;
        const selectedItem = dropdown.querySelector(`.dropdown-item[data-value="${value}"]`);
        if (selectedItem) {
            const trigger = dropdown.querySelector('.dropdown-value');
            if (trigger) {
                trigger.textContent = selectedItem.textContent.trim();
            }
            // Update selected styling
            dropdown.querySelectorAll('.dropdown-item').forEach(item => {
                item.classList.toggle('selected', item.dataset.value === value);
            });
        }
    },

    // ========================================================================
    // Selection Management
    // ========================================================================

    _handleSelectAll() {
        const { matters } = AppState.getFilteredMatters();
        const allSelected = matters.length > 0 && matters.every(m => AppState.selectedMatterIds.includes(m.id));
        if (allSelected) {
            AppState.selectedMatterIds = [];
        } else {
            AppState.selectedMatterIds = matters.map(m => m.id);
        }
        this.render();
    },

    _handleSelectRow(id) {
        const matterId = id;
        const idx = AppState.selectedMatterIds.indexOf(matterId);
        if (idx === -1) {
            AppState.selectedMatterIds.push(matterId);
        } else {
            AppState.selectedMatterIds.splice(idx, 1);
        }
        this.render();
    },

    _handleSort(field) {
        if (AppState.sortField === field) {
            AppState.sortDirection = AppState.sortDirection === 'asc' ? 'desc' : 'asc';
        } else {
            AppState.sortField = field;
            AppState.sortDirection = 'asc';
        }
        AppState.notify();
    },

    // ========================================================================
    // Form Helpers
    // ========================================================================

    _getDefaultFormData() {
        return {
            description: '',
            clientId: null,
            practiceAreaId: null,
            stageId: null,
            responsibleAttorneyId: AppState.currentUser ? AppState.currentUser.id : null,
            originatingAttorneyId: null,
            billingMethod: 'hourly',
            openDate: new Date().toISOString().split('T')[0],
            statuteOfLimitations: '',
            notes: '',
            tags: [],
            customFields: {},
            relationships: [],
            relatedContacts: [],
            documentFolders: [],
            notificationRecipients: [],
            templateId: null
        };
    },

    _getMatterFormData(matterId) {
        const matter = AppState.getMatterById(matterId);
        if (!matter) return this._getDefaultFormData();

        return {
            description: matter.description || '',
            clientId: matter.clientId || null,
            practiceAreaId: matter.practiceAreaId || null,
            stageId: matter.stageId || null,
            responsibleAttorneyId: matter.responsibleAttorneyId || null,
            originatingAttorneyId: matter.originatingAttorneyId || null,
            billingMethod: matter.billingMethod || 'hourly',
            openDate: matter.openDate || '',
            statuteOfLimitations: matter.statuteOfLimitations || '',
            notes: matter.notes || '',
            tags: matter.tags ? [...matter.tags] : [],
            customFields: matter.customFields ? JSON.parse(JSON.stringify(matter.customFields)) : {},
            relationships: matter.relationships ? JSON.parse(JSON.stringify(matter.relationships)) : [],
            relatedContacts: matter.relationships ? JSON.parse(JSON.stringify(matter.relationships)) : [],
            documentFolders: [],
            notificationRecipients: [],
            templateId: null
        };
    },

    _saveMatter() {
        // Sync any live form inputs into _formData
        this._syncFormInputs();

        // Validate required fields
        if (!this._formData.description || !this._formData.description.trim()) {
            this._showToast('Description is required', 'error');
            return;
        }
        if (!this._formData.clientId) {
            this._showToast('Client is required', 'error');
            return;
        }

        const data = {
            description: this._formData.description.trim(),
            clientId: this._formData.clientId,
            practiceAreaId: this._formData.practiceAreaId || null,
            stageId: this._formData.stageId || null,
            responsibleAttorneyId: this._formData.responsibleAttorneyId || null,
            originatingAttorneyId: this._formData.originatingAttorneyId || null,
            billingMethod: this._formData.billingMethod || 'hourly',
            openDate: this._formData.openDate || new Date().toISOString().split('T')[0],
            statuteOfLimitations: this._formData.statuteOfLimitations || null,
            notes: this._formData.notes || '',
            tags: this._formData.tags || [],
            customFields: this._formData.customFields || {},
            relationships: this._formData.relatedContacts || this._formData.relationships || []
        };

        if (AppState.currentMatterId) {
            // Editing
            AppState.updateMatter(AppState.currentMatterId, data);
            window.location.hash = `#/matters/${AppState.currentMatterId}`;
            this._showToast('Matter updated successfully', 'success');
        } else {
            // Creating
            const newMatter = AppState.createMatter(data);
            window.location.hash = `#/matters/${newMatter.id}`;
            this._showToast('Matter created successfully', 'success');
        }
    },

    _syncFormInputs() {
        // Read all data-form-field inputs from the DOM
        const fields = document.querySelectorAll('[data-form-field]');
        fields.forEach(el => {
            this._formData[el.dataset.formField] = el.value;
        });
    },

    _applyTemplate() {
        const templateId = this._formData.templateId;
        if (!templateId) {
            this._showToast('Please select a template first', 'error');
            return;
        }
        const template = AppState.getTemplateById(templateId);
        if (!template) {
            this._showToast('Template not found', 'error');
            return;
        }

        if (template.practiceAreaId) {
            this._formData.practiceAreaId = template.practiceAreaId;
        }
        if (template.billingMethod) {
            this._formData.billingMethod = template.billingMethod;
        }
        if (template.customFields) {
            this._formData.customFields = JSON.parse(JSON.stringify(template.customFields));
        }

        this._showToast('Template applied', 'success');
        this.render();
    },

    // ---- Related contacts in form ----
    _addRelatedContact() {
        if (!this._formData.relatedContacts) {
            this._formData.relatedContacts = [];
        }
        this._formData.relatedContacts.push({
            contactId: null,
            role: '',
            type: ''
        });
        this.render();
    },

    _removeRelatedContact(index) {
        if (this._formData.relatedContacts && index >= 0) {
            this._formData.relatedContacts.splice(index, 1);
            this.render();
        }
    },

    // ---- Document folders in form ----
    _addDocumentFolder() {
        if (!this._formData.documentFolders) {
            this._formData.documentFolders = [];
        }
        this._formData.documentFolders.push({
            id: AppState._nextFolderId++,
            name: 'New Folder'
        });
        this.render();
    },

    _removeDocumentFolder(index) {
        if (this._formData.documentFolders && index >= 0) {
            this._formData.documentFolders.splice(index, 1);
            this.render();
        }
    },

    // ---- Notification recipients in form ----
    _addNotificationRecipient() {
        if (!this._formData.notificationRecipients) {
            this._formData.notificationRecipients = [];
        }
        this._formData.notificationRecipients.push({
            userId: null,
            email: ''
        });
        this.render();
    },

    _removeNotificationRecipient(index) {
        if (this._formData.notificationRecipients && index >= 0) {
            this._formData.notificationRecipients.splice(index, 1);
            this.render();
        }
    },

    // ---- Form section toggle ----
    _toggleFormSection(sectionId) {
        const body = document.querySelector(`#section-${sectionId} .form-section-body`);
        const toggle = document.querySelector(`#section-${sectionId} .section-toggle`);
        if (body) {
            const isHidden = body.style.display === 'none';
            body.style.display = isHidden ? '' : 'none';
            if (toggle) {
                toggle.innerHTML = isHidden ? '&#9660;' : '&#9654;';
            }
            if (isHidden) {
                this._collapsedFormSections.delete(sectionId);
            } else {
                this._collapsedFormSections.add(sectionId);
            }
        }
    },

    // ========================================================================
    // Checkbox and Toggle Handlers
    // ========================================================================

    _handleCheckbox(id) {
        // Checkboxes that map to specific settings or form fields
        if (id.startsWith('notification-')) {
            const key = id.replace('notification-', '');
            const current = AppState.notificationSettings[key];
            AppState.notificationSettings[key] = !current;
            AppState.notify();
        } else if (id.startsWith('form-')) {
            const field = id.replace('form-', '');
            this._formData[field] = !this._formData[field];
            this.render();
        } else if (id.startsWith('modal-')) {
            const field = 'modal_' + id.replace('modal-', '');
            this._formData[field] = !this._formData[field];
        }
    },

    _handleToggle(id) {
        if (id.startsWith('notification-')) {
            const key = id.replace('notification-', '');
            const current = AppState.notificationSettings[key];
            AppState.notificationSettings[key] = !current;
            AppState.notify();
        } else if (id.startsWith('setting-')) {
            const key = id.replace('setting-', '');
            const current = AppState.firmSettings[key];
            AppState.firmSettings[key] = !current;
            AppState.notify();
        } else if (id.startsWith('numbering-')) {
            const key = id.replace('numbering-', '');
            AppState.numberingScheme[key] = !AppState.numberingScheme[key];
            AppState.notify();
        } else if (id.startsWith('form-')) {
            const field = id.replace('form-', '');
            this._formData[field] = !this._formData[field];
            this.render();
        }
    },

    // ========================================================================
    // Modal Helpers
    // ========================================================================

    _showConfirmModal(title, message, callback) {
        this._confirmCallback = callback;
        AppState.modalData = Components.renderConfirmModal(title, message);
        this.render();
    },

    _showStatusPickerModal() {
        const count = AppState.selectedMatterIds.length;
        AppState.modalData = {
            title: `Update Status for ${count} Matter(s)`,
            body: `
                <p>Select the new status for the selected matters:</p>
                <div class="status-picker-options">
                    <button class="btn btn-outline status-option" data-action="confirm-modal" onclick="App._bulkStatusValue='open'" data-bulk-status="open">
                        <span class="matter-status-badge open">Open</span>
                    </button>
                    <button class="btn btn-outline status-option" data-action="confirm-modal" onclick="App._bulkStatusValue='pending'" data-bulk-status="pending">
                        <span class="matter-status-badge pending">Pending</span>
                    </button>
                    <button class="btn btn-outline status-option" data-action="confirm-modal" onclick="App._bulkStatusValue='closed'" data-bulk-status="closed">
                        <span class="matter-status-badge closed">Closed</span>
                    </button>
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            `
        };
        this._confirmCallback = () => {
            const status = App._bulkStatusValue || 'open';
            AppState.bulkUpdateStatus(AppState.selectedMatterIds, status);
            AppState.selectedMatterIds = [];
            this._showToast(`Matters updated to ${status}`, 'success');
        };
        this.render();
    },

    _showDamageFormModal(damageId) {
        const isEdit = !!damageId;
        let damage = null;
        if (isEdit) {
            damage = AppState.damages.find(d => d.id === damageId);
        }

        this._formData.modal_type = damage ? damage.type : 'general';
        this._formData.modal_description = damage ? damage.description : '';
        this._formData.modal_amount = damage ? damage.amount : '';
        this._formData.modal_date = damage ? damage.date : '';
        this._formData.modal_notes = damage ? damage.notes : '';
        this._formData.modal_editId = damageId || null;

        const damageTypes = [
            { value: 'general', label: 'General Damages' },
            { value: 'special', label: 'Special Damages' },
            { value: 'economic', label: 'Economic Loss' },
            { value: 'non-economic', label: 'Non-Economic Loss' },
            { value: 'punitive', label: 'Punitive Damages' },
            { value: 'property', label: 'Property Damage' },
            { value: 'lost-wages', label: 'Lost Wages' },
            { value: 'medical', label: 'Medical Expenses' },
            { value: 'pain-suffering', label: 'Pain & Suffering' },
            { value: 'future-medical', label: 'Future Medical' },
            { value: 'loss-of-consortium', label: 'Loss of Consortium' }
        ];

        AppState.modalData = {
            title: isEdit ? 'Edit Damage' : 'Add Damage',
            body: `
                <div class="form-group">
                    <label>Type</label>
                    ${Components.renderDropdown('modal-type', damageTypes, this._formData.modal_type, 'Select type...')}
                </div>
                <div class="form-group">
                    <label>Description <span class="required">*</span></label>
                    <input type="text" class="form-control" data-form-field="modal_description" value="${this._escapeAttr(this._formData.modal_description)}" placeholder="Enter description..." />
                </div>
                <div class="form-group">
                    <label>Amount ($)</label>
                    <input type="number" class="form-control" data-form-field="modal_amount" value="${this._formData.modal_amount}" step="0.01" placeholder="0.00" />
                </div>
                <div class="form-group">
                    <label>Date</label>
                    <input type="date" class="form-control" data-form-field="modal_date" value="${this._escapeAttr(this._formData.modal_date || '')}" />
                </div>
                <div class="form-group">
                    <label>Notes</label>
                    <textarea class="form-control" data-form-field="modal_notes" rows="3" placeholder="Additional notes...">${this._escapeAttr(this._formData.modal_notes)}</textarea>
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="save-damage">Save</button>
            `
        };
        this.render();
    },

    _showProviderFormModal(providerId) {
        const isEdit = !!providerId;
        let provider = null;
        if (isEdit) {
            provider = AppState.medicalProviders.find(p => p.id === providerId);
        }

        this._formData.modal_name = provider ? provider.name : '';
        this._formData.modal_specialty = provider ? provider.specialty : '';
        this._formData.modal_phone = provider ? provider.phone : '';
        this._formData.modal_fax = provider ? provider.fax : '';
        this._formData.modal_address = provider ? provider.address : '';
        this._formData.modal_notes = provider ? provider.notes : '';
        this._formData.modal_editId = providerId || null;

        AppState.modalData = {
            title: isEdit ? 'Edit Medical Provider' : 'Add Medical Provider',
            body: `
                <div class="form-group">
                    <label>Provider Name <span class="required">*</span></label>
                    <input type="text" class="form-control" data-form-field="modal_name" value="${this._escapeAttr(this._formData.modal_name)}" placeholder="Enter provider name..." />
                </div>
                <div class="form-group">
                    <label>Specialty</label>
                    <input type="text" class="form-control" data-form-field="modal_specialty" value="${this._escapeAttr(this._formData.modal_specialty)}" placeholder="e.g., Orthopedics, Neurology..." />
                </div>
                <div class="form-row">
                    <div class="form-group half">
                        <label>Phone</label>
                        <input type="text" class="form-control" data-form-field="modal_phone" value="${this._escapeAttr(this._formData.modal_phone)}" placeholder="(555) 555-5555" />
                    </div>
                    <div class="form-group half">
                        <label>Fax</label>
                        <input type="text" class="form-control" data-form-field="modal_fax" value="${this._escapeAttr(this._formData.modal_fax)}" placeholder="(555) 555-5555" />
                    </div>
                </div>
                <div class="form-group">
                    <label>Address</label>
                    <input type="text" class="form-control" data-form-field="modal_address" value="${this._escapeAttr(this._formData.modal_address)}" placeholder="Full address..." />
                </div>
                <div class="form-group">
                    <label>Notes</label>
                    <textarea class="form-control" data-form-field="modal_notes" rows="3" placeholder="Additional notes...">${this._escapeAttr(this._formData.modal_notes)}</textarea>
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="save-provider">Save</button>
            `
        };
        this.render();
    },

    _showRecoveryFormModal(recoveryId) {
        const isEdit = !!recoveryId;
        let recovery = null;
        if (isEdit) {
            const settlement = AppState.getSettlement(AppState.currentMatterId);
            recovery = settlement.recoveries.find(r => r.id === recoveryId);
        }

        this._formData.modal_type = recovery ? recovery.type : 'settlement';
        this._formData.modal_amount = recovery ? recovery.amount : '';
        this._formData.modal_date = recovery ? recovery.date : '';
        this._formData.modal_source = recovery ? recovery.source : '';
        this._formData.modal_notes = recovery ? recovery.notes : '';
        this._formData.modal_editId = recoveryId || null;

        const recoveryTypes = [
            { value: 'settlement', label: 'Settlement' },
            { value: 'verdict', label: 'Verdict' },
            { value: 'judgment', label: 'Judgment' },
            { value: 'insurance', label: 'Insurance Payment' },
            { value: 'other', label: 'Other' }
        ];

        AppState.modalData = {
            title: isEdit ? 'Edit Recovery' : 'Add Recovery',
            body: `
                <div class="form-group">
                    <label>Type</label>
                    ${Components.renderDropdown('modal-type', recoveryTypes, this._formData.modal_type, 'Select type...')}
                </div>
                <div class="form-group">
                    <label>Amount ($) <span class="required">*</span></label>
                    <input type="number" class="form-control" data-form-field="modal_amount" value="${this._formData.modal_amount}" step="0.01" placeholder="0.00" />
                </div>
                <div class="form-group">
                    <label>Date</label>
                    <input type="date" class="form-control" data-form-field="modal_date" value="${this._escapeAttr(this._formData.modal_date || '')}" />
                </div>
                <div class="form-group">
                    <label>Source</label>
                    <input type="text" class="form-control" data-form-field="modal_source" value="${this._escapeAttr(this._formData.modal_source)}" placeholder="e.g., Defendant's insurance..." />
                </div>
                <div class="form-group">
                    <label>Notes</label>
                    <textarea class="form-control" data-form-field="modal_notes" rows="3" placeholder="Additional notes...">${this._escapeAttr(this._formData.modal_notes)}</textarea>
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="save-recovery">Save</button>
            `
        };
        this.render();
    },

    _showLegalFeeFormModal(feeId) {
        const isEdit = !!feeId;
        let fee = null;
        if (isEdit) {
            const settlement = AppState.getSettlement(AppState.currentMatterId);
            fee = settlement.legalFees.find(f => f.id === feeId);
        }

        this._formData.modal_type = fee ? fee.type : 'contingency';
        this._formData.modal_description = fee ? fee.description : '';
        this._formData.modal_percentage = fee ? fee.percentage : '';
        this._formData.modal_flatAmount = fee ? fee.flatAmount : '';
        this._formData.modal_notes = fee ? fee.notes : '';
        this._formData.modal_editId = feeId || null;

        const feeTypes = [
            { value: 'contingency', label: 'Contingency Fee' },
            { value: 'flat', label: 'Flat Fee' },
            { value: 'hourly', label: 'Hourly Fee' },
            { value: 'retainer', label: 'Retainer' },
            { value: 'referral', label: 'Referral Fee' },
            { value: 'other', label: 'Other' }
        ];

        AppState.modalData = {
            title: isEdit ? 'Edit Legal Fee' : 'Add Legal Fee',
            body: `
                <div class="form-group">
                    <label>Fee Type</label>
                    ${Components.renderDropdown('modal-type', feeTypes, this._formData.modal_type, 'Select type...')}
                </div>
                <div class="form-group">
                    <label>Description</label>
                    <input type="text" class="form-control" data-form-field="modal_description" value="${this._escapeAttr(this._formData.modal_description)}" placeholder="Fee description..." />
                </div>
                <div class="form-row">
                    <div class="form-group half">
                        <label>Percentage (%)</label>
                        <input type="number" class="form-control" data-form-field="modal_percentage" value="${this._formData.modal_percentage}" step="0.1" min="0" max="100" placeholder="e.g., 33.33" />
                    </div>
                    <div class="form-group half">
                        <label>Flat Amount ($)</label>
                        <input type="number" class="form-control" data-form-field="modal_flatAmount" value="${this._formData.modal_flatAmount}" step="0.01" placeholder="0.00" />
                    </div>
                </div>
                <div class="form-group">
                    <label>Notes</label>
                    <textarea class="form-control" data-form-field="modal_notes" rows="3" placeholder="Additional notes...">${this._escapeAttr(this._formData.modal_notes)}</textarea>
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="save-legal-fee">Save</button>
            `
        };
        this.render();
    },

    _showLienFormModal(lienId) {
        const isEdit = !!lienId;
        let lien = null;
        if (isEdit) {
            const settlement = AppState.getSettlement(AppState.currentMatterId);
            lien = settlement.nonMedicalLiens.find(l => l.id === lienId);
        }

        this._formData.modal_lienholder = lien ? lien.lienholder : '';
        this._formData.modal_type = lien ? lien.type : 'other';
        this._formData.modal_amount = lien ? lien.amount : '';
        this._formData.modal_negotiatedAmount = lien ? (lien.negotiatedAmount != null ? lien.negotiatedAmount : '') : '';
        this._formData.modal_status = lien ? lien.status : 'pending';
        this._formData.modal_notes = lien ? lien.notes : '';
        this._formData.modal_editId = lienId || null;

        const lienTypes = [
            { value: 'child-support', label: 'Child Support' },
            { value: 'government', label: 'Government' },
            { value: 'workers-comp', label: 'Workers Compensation' },
            { value: 'medicaid', label: 'Medicaid' },
            { value: 'medicare', label: 'Medicare' },
            { value: 'erisa', label: 'ERISA' },
            { value: 'va', label: 'VA Benefits' },
            { value: 'other', label: 'Other' }
        ];

        const statusOptions = [
            { value: 'pending', label: 'Pending' },
            { value: 'negotiating', label: 'Negotiating' },
            { value: 'resolved', label: 'Resolved' },
            { value: 'paid', label: 'Paid' }
        ];

        AppState.modalData = {
            title: isEdit ? 'Edit Lien' : 'Add Lien',
            body: `
                <div class="form-group">
                    <label>Lienholder <span class="required">*</span></label>
                    <input type="text" class="form-control" data-form-field="modal_lienholder" value="${this._escapeAttr(this._formData.modal_lienholder)}" placeholder="Enter lienholder name..." />
                </div>
                <div class="form-group">
                    <label>Lien Type</label>
                    ${Components.renderDropdown('modal-type', lienTypes, this._formData.modal_type, 'Select type...')}
                </div>
                <div class="form-row">
                    <div class="form-group half">
                        <label>Original Amount ($)</label>
                        <input type="number" class="form-control" data-form-field="modal_amount" value="${this._formData.modal_amount}" step="0.01" placeholder="0.00" />
                    </div>
                    <div class="form-group half">
                        <label>Negotiated Amount ($)</label>
                        <input type="number" class="form-control" data-form-field="modal_negotiatedAmount" value="${this._formData.modal_negotiatedAmount}" step="0.01" placeholder="Leave blank if not negotiated" />
                    </div>
                </div>
                <div class="form-group">
                    <label>Status</label>
                    ${Components.renderDropdown('modal-status', statusOptions, this._formData.modal_status, 'Select status...')}
                </div>
                <div class="form-group">
                    <label>Notes</label>
                    <textarea class="form-control" data-form-field="modal_notes" rows="3" placeholder="Additional notes...">${this._escapeAttr(this._formData.modal_notes)}</textarea>
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="save-lien">Save</button>
            `
        };
        this.render();
    },

    _showOutstandingBalanceFormModal(balanceId) {
        const isEdit = !!balanceId;
        let balance = null;
        if (isEdit) {
            const settlement = AppState.getSettlement(AppState.currentMatterId);
            balance = settlement.outstandingBalances.find(b => b.id === balanceId);
        }

        this._formData.modal_creditor = balance ? balance.creditor : '';
        this._formData.modal_type = balance ? balance.type : 'medical';
        this._formData.modal_originalAmount = balance ? balance.originalAmount : '';
        this._formData.modal_negotiatedAmount = balance ? (balance.negotiatedAmount != null ? balance.negotiatedAmount : '') : '';
        this._formData.modal_status = balance ? balance.status : 'outstanding';
        this._formData.modal_notes = balance ? balance.notes : '';
        this._formData.modal_editId = balanceId || null;

        const balanceTypes = [
            { value: 'medical', label: 'Medical' },
            { value: 'legal', label: 'Legal' },
            { value: 'personal', label: 'Personal' },
            { value: 'insurance', label: 'Insurance Subrogation' },
            { value: 'other', label: 'Other' }
        ];

        const statusOptions = [
            { value: 'outstanding', label: 'Outstanding' },
            { value: 'negotiating', label: 'Negotiating' },
            { value: 'resolved', label: 'Resolved' },
            { value: 'paid', label: 'Paid' }
        ];

        AppState.modalData = {
            title: isEdit ? 'Edit Outstanding Balance' : 'Add Outstanding Balance',
            body: `
                <div class="form-group">
                    <label>Creditor <span class="required">*</span></label>
                    <input type="text" class="form-control" data-form-field="modal_creditor" value="${this._escapeAttr(this._formData.modal_creditor)}" placeholder="Enter creditor name..." />
                </div>
                <div class="form-group">
                    <label>Type</label>
                    ${Components.renderDropdown('modal-type', balanceTypes, this._formData.modal_type, 'Select type...')}
                </div>
                <div class="form-row">
                    <div class="form-group half">
                        <label>Original Amount ($)</label>
                        <input type="number" class="form-control" data-form-field="modal_originalAmount" value="${this._formData.modal_originalAmount}" step="0.01" placeholder="0.00" />
                    </div>
                    <div class="form-group half">
                        <label>Negotiated Amount ($)</label>
                        <input type="number" class="form-control" data-form-field="modal_negotiatedAmount" value="${this._formData.modal_negotiatedAmount}" step="0.01" placeholder="Leave blank if not negotiated" />
                    </div>
                </div>
                <div class="form-group">
                    <label>Status</label>
                    ${Components.renderDropdown('modal-status', statusOptions, this._formData.modal_status, 'Select status...')}
                </div>
                <div class="form-group">
                    <label>Notes</label>
                    <textarea class="form-control" data-form-field="modal_notes" rows="3" placeholder="Additional notes...">${this._escapeAttr(this._formData.modal_notes)}</textarea>
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="save-outstanding-balance">Save</button>
            `
        };
        this.render();
    },

    _showPracticeAreaFormModal(paId) {
        const isEdit = !!paId;
        let pa = null;
        if (isEdit) {
            pa = AppState.getPracticeAreaById(paId);
        }

        this._formData.modal_name = pa ? pa.name : '';
        this._formData.modal_description = pa ? pa.description : '';
        this._formData.modal_color = pa ? pa.color : '#6366f1';
        this._formData.modal_editId = paId || null;

        AppState.modalData = {
            title: isEdit ? 'Edit Practice Area' : 'Add Practice Area',
            body: `
                <div class="form-group">
                    <label>Name <span class="required">*</span></label>
                    <input type="text" class="form-control" data-form-field="modal_name" value="${this._escapeAttr(this._formData.modal_name)}" placeholder="e.g., Personal Injury, Family Law..." />
                </div>
                <div class="form-group">
                    <label>Description</label>
                    <textarea class="form-control" data-form-field="modal_description" rows="3" placeholder="Describe this practice area...">${this._escapeAttr(this._formData.modal_description)}</textarea>
                </div>
                <div class="form-group">
                    <label>Color</label>
                    <input type="color" class="form-control color-input" data-form-field="modal_color" value="${this._formData.modal_color}" />
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="save-practice-area">Save</button>
            `
        };
        this.render();
    },

    _showStageFormModal(practiceAreaId, stageId) {
        const isEdit = !!stageId;
        let stage = null;
        if (isEdit) {
            const pa = AppState.getPracticeAreaById(practiceAreaId);
            if (pa && pa.stages) {
                stage = pa.stages.find(s => s.id === stageId);
            }
        }

        this._formData.modal_name = stage ? stage.name : '';
        this._formData.modal_practiceAreaId = practiceAreaId;
        this._formData.modal_editId = stageId || null;

        AppState.modalData = {
            title: isEdit ? 'Edit Stage' : 'Add Stage',
            body: `
                <div class="form-group">
                    <label>Stage Name <span class="required">*</span></label>
                    <input type="text" class="form-control" data-form-field="modal_name" value="${this._escapeAttr(this._formData.modal_name)}" placeholder="e.g., Investigation, Discovery, Trial..." />
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="save-stage">Save</button>
            `
        };
        this.render();
    },

    _showTemplateFormModal(templateId) {
        const isEdit = !!templateId;
        let template = null;
        if (isEdit) {
            template = AppState.getTemplateById(templateId);
        }

        this._formData.modal_name = template ? template.name : '';
        this._formData.modal_description = template ? template.description : '';
        this._formData.modal_practiceAreaId = template ? template.practiceAreaId : null;
        this._formData.modal_billingMethod = template ? template.billingMethod : 'hourly';
        this._formData.modal_editId = templateId || null;

        const paOptions = AppState.practiceAreas.map(pa => ({ value: pa.id, label: pa.name }));
        paOptions.unshift({ value: '', label: 'None' });

        const billingOptions = [
            { value: 'hourly', label: 'Hourly' },
            { value: 'flat', label: 'Flat Fee' },
            { value: 'contingency', label: 'Contingency' },
            { value: 'retainer', label: 'Retainer' },
            { value: 'pro-bono', label: 'Pro Bono' }
        ];

        AppState.modalData = {
            title: isEdit ? 'Edit Template' : 'Create Template',
            body: `
                <div class="form-group">
                    <label>Template Name <span class="required">*</span></label>
                    <input type="text" class="form-control" data-form-field="modal_name" value="${this._escapeAttr(this._formData.modal_name)}" placeholder="Enter template name..." />
                </div>
                <div class="form-group">
                    <label>Description</label>
                    <textarea class="form-control" data-form-field="modal_description" rows="3" placeholder="Template description...">${this._escapeAttr(this._formData.modal_description)}</textarea>
                </div>
                <div class="form-group">
                    <label>Practice Area</label>
                    ${Components.renderDropdown('modal-practiceAreaId', paOptions, this._formData.modal_practiceAreaId, 'Select practice area...')}
                </div>
                <div class="form-group">
                    <label>Billing Method</label>
                    ${Components.renderDropdown('modal-billingMethod', billingOptions, this._formData.modal_billingMethod, 'Select billing method...')}
                </div>
            `,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="save-template">Save</button>
            `
        };
        this.render();
    },

    // ========================================================================
    // Save Handlers for Modals
    // ========================================================================

    _saveDamage() {
        this._syncModalInputs();

        const description = this._formData.modal_description;
        if (!description || !description.trim()) {
            this._showToast('Description is required', 'error');
            return;
        }

        const data = {
            matterId: AppState.currentMatterId,
            type: this._formData.modal_type || 'general',
            description: description.trim(),
            amount: parseFloat(this._formData.modal_amount) || 0,
            date: this._formData.modal_date || null,
            notes: this._formData.modal_notes || ''
        };

        if (this._formData.modal_editId) {
            AppState.updateDamage(this._formData.modal_editId, data);
            this._showToast('Damage updated', 'success');
        } else {
            AppState.createDamage(data);
            this._showToast('Damage added', 'success');
        }

        AppState.modalData = null;
        this.render();
    },

    _saveMedicalProvider() {
        this._syncModalInputs();

        const name = this._formData.modal_name;
        if (!name || !name.trim()) {
            this._showToast('Provider name is required', 'error');
            return;
        }

        const data = {
            matterId: AppState.currentMatterId,
            name: name.trim(),
            specialty: this._formData.modal_specialty || '',
            phone: this._formData.modal_phone || '',
            fax: this._formData.modal_fax || '',
            address: this._formData.modal_address || '',
            notes: this._formData.modal_notes || ''
        };

        if (this._formData.modal_editId) {
            AppState.updateMedicalProvider(this._formData.modal_editId, data);
            this._showToast('Provider updated', 'success');
        } else {
            AppState.createMedicalProvider(data);
            this._showToast('Provider added', 'success');
        }

        AppState.modalData = null;
        this.render();
    },

    _saveRecovery() {
        this._syncModalInputs();

        const amount = parseFloat(this._formData.modal_amount);
        if (!amount || amount <= 0) {
            this._showToast('Amount must be greater than zero', 'error');
            return;
        }

        const data = {
            type: this._formData.modal_type || 'settlement',
            amount: amount,
            date: this._formData.modal_date || null,
            source: this._formData.modal_source || '',
            notes: this._formData.modal_notes || ''
        };

        if (this._formData.modal_editId) {
            AppState.updateRecovery(AppState.currentMatterId, this._formData.modal_editId, data);
            this._showToast('Recovery updated', 'success');
        } else {
            AppState.addRecovery(AppState.currentMatterId, data);
            this._showToast('Recovery added', 'success');
        }

        AppState.modalData = null;
        this.render();
    },

    _saveLegalFee() {
        this._syncModalInputs();

        const data = {
            type: this._formData.modal_type || 'contingency',
            description: this._formData.modal_description || '',
            percentage: parseFloat(this._formData.modal_percentage) || 0,
            flatAmount: parseFloat(this._formData.modal_flatAmount) || 0,
            notes: this._formData.modal_notes || ''
        };

        if (data.percentage === 0 && data.flatAmount === 0) {
            this._showToast('Please enter a percentage or flat amount', 'error');
            return;
        }

        if (this._formData.modal_editId) {
            AppState.updateLegalFee(AppState.currentMatterId, this._formData.modal_editId, data);
            this._showToast('Legal fee updated', 'success');
        } else {
            AppState.addLegalFee(AppState.currentMatterId, data);
            this._showToast('Legal fee added', 'success');
        }

        AppState.modalData = null;
        this.render();
    },

    _saveLien() {
        this._syncModalInputs();

        const lienholder = this._formData.modal_lienholder;
        if (!lienholder || !lienholder.trim()) {
            this._showToast('Lienholder is required', 'error');
            return;
        }

        const negotiatedRaw = this._formData.modal_negotiatedAmount;
        const data = {
            lienholder: lienholder.trim(),
            type: this._formData.modal_type || 'other',
            amount: parseFloat(this._formData.modal_amount) || 0,
            negotiatedAmount: negotiatedRaw !== '' && negotiatedRaw !== null && negotiatedRaw !== undefined ? parseFloat(negotiatedRaw) : null,
            status: this._formData.modal_status || 'pending',
            notes: this._formData.modal_notes || ''
        };

        if (this._formData.modal_editId) {
            AppState.updateNonMedicalLien(AppState.currentMatterId, this._formData.modal_editId, data);
            this._showToast('Lien updated', 'success');
        } else {
            AppState.addNonMedicalLien(AppState.currentMatterId, data);
            this._showToast('Lien added', 'success');
        }

        AppState.modalData = null;
        this.render();
    },

    _saveOutstandingBalance() {
        this._syncModalInputs();

        const creditor = this._formData.modal_creditor;
        if (!creditor || !creditor.trim()) {
            this._showToast('Creditor is required', 'error');
            return;
        }

        const negotiatedRaw = this._formData.modal_negotiatedAmount;
        const data = {
            creditor: creditor.trim(),
            type: this._formData.modal_type || 'medical',
            originalAmount: parseFloat(this._formData.modal_originalAmount) || 0,
            negotiatedAmount: negotiatedRaw !== '' && negotiatedRaw !== null && negotiatedRaw !== undefined ? parseFloat(negotiatedRaw) : null,
            status: this._formData.modal_status || 'outstanding',
            notes: this._formData.modal_notes || ''
        };

        if (this._formData.modal_editId) {
            AppState.updateOutstandingBalance(AppState.currentMatterId, this._formData.modal_editId, data);
            this._showToast('Balance updated', 'success');
        } else {
            AppState.addOutstandingBalance(AppState.currentMatterId, data);
            this._showToast('Balance added', 'success');
        }

        AppState.modalData = null;
        this.render();
    },

    _savePracticeArea() {
        this._syncModalInputs();

        const name = this._formData.modal_name;
        if (!name || !name.trim()) {
            this._showToast('Name is required', 'error');
            return;
        }

        const data = {
            name: name.trim(),
            description: this._formData.modal_description || '',
            color: this._formData.modal_color || '#6366f1'
        };

        if (this._formData.modal_editId) {
            AppState.updatePracticeArea(this._formData.modal_editId, data);
            this._showToast('Practice area updated', 'success');
        } else {
            AppState.createPracticeArea(data);
            this._showToast('Practice area created', 'success');
        }

        AppState.modalData = null;
        this.render();
    },

    _saveStage() {
        this._syncModalInputs();

        const name = this._formData.modal_name;
        if (!name || !name.trim()) {
            this._showToast('Stage name is required', 'error');
            return;
        }

        const practiceAreaId = this._formData.modal_practiceAreaId;
        if (!practiceAreaId) {
            this._showToast('Practice area not found', 'error');
            return;
        }

        if (this._formData.modal_editId) {
            AppState.updateStage(practiceAreaId, this._formData.modal_editId, name.trim());
            this._showToast('Stage updated', 'success');
        } else {
            const result = AppState.createStage(practiceAreaId, name.trim());
            if (result === null) {
                this._showToast('Maximum 15 stages per practice area', 'error');
                return;
            }
            this._showToast('Stage created', 'success');
        }

        AppState.modalData = null;
        this.render();
    },

    _saveTemplate() {
        this._syncModalInputs();

        const name = this._formData.modal_name;
        if (!name || !name.trim()) {
            this._showToast('Template name is required', 'error');
            return;
        }

        const data = {
            name: name.trim(),
            description: this._formData.modal_description || '',
            practiceAreaId: this._formData.modal_practiceAreaId || null,
            billingMethod: this._formData.modal_billingMethod || 'hourly'
        };

        if (this._formData.modal_editId) {
            AppState.updateTemplate(this._formData.modal_editId, data);
            this._showToast('Template updated', 'success');
        } else {
            AppState.createTemplate(data);
            this._showToast('Template created', 'success');
        }

        AppState.modalData = null;
        this.render();
    },

    _saveNumberingScheme() {
        this._syncFormInputs();

        const data = {};
        const prefixEl = document.querySelector('[data-form-field="numbering_prefix"]');
        const separatorEl = document.querySelector('[data-form-field="numbering_separator"]');
        const padLengthEl = document.querySelector('[data-form-field="numbering_padLength"]');

        if (prefixEl) data.prefix = prefixEl.value;
        if (separatorEl) data.separator = separatorEl.value;
        if (padLengthEl) data.padLength = parseInt(padLengthEl.value) || 5;
        data.appendClientName = !!AppState.numberingScheme.appendClientName;

        AppState.updateNumberingScheme(data);
        this._showToast('Numbering scheme saved', 'success');
    },

    _saveNotificationSettings() {
        // Notification toggle states are already saved in real-time via _handleToggle
        AppState.notify();
        this._showToast('Notification settings saved', 'success');
    },

    // ========================================================================
    // Settings Helpers
    // ========================================================================

    _deletePracticeArea(id) {
        const mattersUsing = AppState.getMattersForPracticeArea(id);
        if (mattersUsing.length > 0) {
            this._showToast(`Cannot delete: ${mattersUsing.length} matter(s) use this practice area`, 'error');
            return;
        }
        this._showConfirmModal('Delete Practice Area',
            'Are you sure you want to delete this practice area and all its stages?',
            () => {
                const result = AppState.deletePracticeArea(id);
                if (result) {
                    this._showToast('Practice area deleted', 'success');
                } else {
                    this._showToast('Cannot delete practice area with assigned matters', 'error');
                }
            });
    },

    _togglePracticeAreaStages(id) {
        if (this._expandedPracticeAreas.has(id)) {
            this._expandedPracticeAreas.delete(id);
        } else {
            this._expandedPracticeAreas.add(id);
        }
        this.render();
    },

    // ========================================================================
    // Export
    // ========================================================================

    _exportMattersCSV() {
        const headers = ['Number', 'Description', 'Status', 'Client', 'Practice Area', 'Responsible Attorney', 'Billing Method', 'Open Date', 'Closed Date'];
        const rows = AppState.matters.map(m => {
            const client = m.clientId ? AppState.getContactById(m.clientId) : null;
            const clientName = client ? (client.name || ((client.firstName || '') + ' ' + (client.lastName || '')).trim()) : '';
            const pa = m.practiceAreaId ? AppState.getPracticeAreaById(m.practiceAreaId) : null;
            const attorney = m.responsibleAttorneyId ? AppState.getUserById(m.responsibleAttorneyId) : null;

            return [
                AppState.formatMatterNumber(m),
                this._csvEscape(m.description),
                m.status,
                this._csvEscape(clientName),
                pa ? this._csvEscape(pa.name) : '',
                attorney ? this._csvEscape(attorney.name) : '',
                m.billingMethod || '',
                m.openDate || '',
                m.closedDate || ''
            ].join(',');
        });

        const csv = [headers.join(','), ...rows].join('\n');
        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);

        const link = document.createElement('a');
        link.href = url;
        link.download = `matters_export_${new Date().toISOString().split('T')[0]}.csv`;
        link.style.display = 'none';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);

        this._showToast('Matters exported to CSV', 'success');
    },

    _csvEscape(str) {
        if (!str) return '';
        str = String(str);
        if (str.includes(',') || str.includes('"') || str.includes('\n')) {
            return '"' + str.replace(/"/g, '""') + '"';
        }
        return str;
    },

    // ========================================================================
    // Provider Section Toggle (Medical Records tab)
    // ========================================================================

    _toggleProviderSection(providerId, section) {
        const key = `${providerId}_${section}`;
        if (!this._expandedProviderSections[key]) {
            this._expandedProviderSections[key] = true;
        } else {
            delete this._expandedProviderSections[key];
        }
        this.render();
    },

    // ========================================================================
    // Toast Notifications
    // ========================================================================

    _showToast(message, type) {
        const container = document.getElementById('toastContainer');
        if (!container) return;

        const toastHtml = Components.renderToast(message, type || 'info');
        container.insertAdjacentHTML('beforeend', toastHtml);

        // Get the toast element just added
        const toasts = container.querySelectorAll('.toast');
        const lastToast = toasts[toasts.length - 1];

        if (lastToast) {
            setTimeout(() => {
                lastToast.classList.add('fade-out');
                setTimeout(() => {
                    lastToast.remove();
                }, 300);
            }, 3000);
        }
    },

    // ========================================================================
    // Utility
    // ========================================================================

    _escapeAttr(str) {
        if (str === null || str === undefined) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    },

    _syncModalInputs() {
        // Read all data-form-field inputs from the modal
        const modalBody = document.getElementById('modalBody');
        if (!modalBody) return;
        const fields = modalBody.querySelectorAll('[data-form-field]');
        fields.forEach(el => {
            this._formData[el.dataset.formField] = el.value;
        });
    }
};

// ========================================================================
// Bootstrap
// ========================================================================

document.addEventListener('DOMContentLoaded', () => App.init());
