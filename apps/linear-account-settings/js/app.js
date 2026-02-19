// ============================================================
// app.js — Router, event handlers, and application initialization
// ============================================================

const ROUTES = {
    '/profile': { view: 'profile', label: 'Profile' },
    '/preferences': { view: 'preferences', label: 'Preferences' },
    '/notifications': { view: 'notifications', label: 'Notifications' },
    '/security': { view: 'security', label: 'Security & Access' }
};

// ---- Router ----

function navigate(path) {
    AppState.currentRoute = path;
    AppState.routeParams = {};
    AppState.validationErrors = {};
    window.location.hash = '#' + path;
    render();
}

function render() {
    const route = ROUTES[AppState.currentRoute];
    if (!route) {
        navigate('/profile');
        return;
    }

    const contentEl = document.getElementById('contentWrapper');
    const viewFn = Views[route.view];
    if (viewFn) {
        contentEl.innerHTML = viewFn();
    }

    // Update sidebar active state
    document.querySelectorAll('.sidebar-item').forEach(item => {
        const itemRoute = item.getAttribute('data-route');
        item.classList.toggle('active', itemRoute === AppState.currentRoute);
    });

    // Update user avatar in topbar
    const avatarEl = document.getElementById('currentUserAvatar');
    if (avatarEl) {
        avatarEl.innerHTML = Components.avatar(AppState.currentUser, 28);
    }

    attachHandlers();
}

// ---- Event Handlers ----

function attachHandlers() {
    // Route links
    document.querySelectorAll('[data-route]').forEach(el => {
        if (el._handlerAttached) return;
        el._handlerAttached = true;
        el.addEventListener('click', (e) => {
            e.preventDefault();
            navigate(el.getAttribute('data-route'));
        });
    });

    // Custom dropdown handling
    document.querySelectorAll('.custom-dropdown').forEach(dd => {
        if (dd._handlerAttached || dd.classList.contains('disabled')) return;
        dd._handlerAttached = true;

        const trigger = dd.querySelector('.dropdown-trigger');
        const menu = dd.querySelector('.dropdown-menu');

        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            // Close all other dropdowns
            document.querySelectorAll('.custom-dropdown.open').forEach(other => {
                if (other !== dd) other.classList.remove('open');
            });
            dd.classList.toggle('open');
        });

        menu.querySelectorAll('.dropdown-item').forEach(item => {
            item.addEventListener('click', (e) => {
                e.stopPropagation();
                const value = item.getAttribute('data-value');
                dd.setAttribute('data-value', value);
                trigger.innerHTML = item.textContent + '<span class="dropdown-arrow">&#9662;</span>';
                menu.querySelectorAll('.dropdown-item').forEach(i => i.classList.remove('selected'));
                item.classList.add('selected');
                dd.classList.remove('open');
                handleDropdownChange(dd.id, value);
            });
        });
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', () => {
        document.querySelectorAll('.custom-dropdown.open').forEach(dd => {
            dd.classList.remove('open');
        });
    });

    // Toggle switches
    document.querySelectorAll('.toggle-switch:not(.mini)').forEach(toggle => {
        if (toggle._handlerAttached || toggle.classList.contains('disabled')) return;
        toggle._handlerAttached = true;
        toggle.addEventListener('click', () => {
            const isOn = toggle.getAttribute('data-checked') === 'true';
            const newState = !isOn;
            toggle.setAttribute('data-checked', String(newState));
            toggle.setAttribute('aria-checked', String(newState));
            toggle.classList.toggle('on', newState);
            toggle.classList.toggle('off', !newState);
            handleToggleChange(toggle.id, newState);
        });
        toggle.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                toggle.click();
            }
        });
    });

    // Mini toggle switches (notification groups)
    document.querySelectorAll('.toggle-switch.mini').forEach(toggle => {
        if (toggle._handlerAttached || toggle.classList.contains('disabled')) return;
        toggle._handlerAttached = true;
        toggle.addEventListener('click', () => {
            const isOn = toggle.getAttribute('data-checked') === 'true';
            const newState = !isOn;
            toggle.setAttribute('data-checked', String(newState));
            toggle.setAttribute('aria-checked', String(newState));
            toggle.classList.toggle('on', newState);
            toggle.classList.toggle('off', !newState);

            const groupId = toggle.getAttribute('data-group-id');
            const channelId = toggle.getAttribute('data-channel-id');
            if (groupId && channelId) {
                AppState.updateNotificationGroup(groupId, channelId, newState);
            }
        });
    });

    // Action buttons
    document.querySelectorAll('[data-action]').forEach(btn => {
        if (btn._handlerAttached) return;
        btn._handlerAttached = true;
        btn.addEventListener('click', (e) => {
            handleAction(btn.getAttribute('data-action'), btn, e);
        });
    });
}

// ---- Dropdown Change Handler ----

function handleDropdownChange(id, value) {
    switch (id) {
        // Preferences dropdowns
        case 'defaultHomeView':
            AppState.updatePreference('defaultHomeView', value);
            break;
        case 'firstDayOfWeek':
            AppState.updatePreference('firstDayOfWeek', value);
            break;
        case 'fontSize':
            AppState.updatePreference('fontSize', value);
            break;
        case 'theme':
            AppState.updatePreference('theme', value);
            break;
        case 'gitAttachmentFormat':
            AppState.updatePreference('gitAttachmentFormat', value);
            break;
        // Profile dropdowns
        case 'profileTimezone':
            // Saved on button click, not dropdown change
            break;
    }
}

// ---- Toggle Change Handler ----

function handleToggleChange(id, value) {
    switch (id) {
        // Preferences toggles
        case 'displayFullNames':
            AppState.updatePreference('displayFullNames', value);
            break;
        case 'convertTextEmoticons':
            AppState.updatePreference('convertTextEmoticons', value);
            break;
        case 'cursorPointer':
            AppState.updatePreference('cursorPointer', value);
            break;
        case 'openLinearURLsInDesktopApp':
            AppState.updatePreference('openLinearURLsInDesktopApp', value);
            break;
        case 'notificationBadge':
            AppState.updatePreference('notificationBadge', value);
            break;
        case 'spellCheck':
            AppState.updatePreference('spellCheck', value);
            break;
        case 'autoAssignOnCreate':
            AppState.updatePreference('autoAssignOnCreate', value);
            break;
        case 'autoAssignOnStarted':
            AppState.updatePreference('autoAssignOnStarted', value);
            break;
        case 'gitBranchMoveToStarted':
            AppState.updatePreference('gitBranchMoveToStarted', value);
            break;
        case 'gitBranchAutoAssign':
            AppState.updatePreference('gitBranchAutoAssign', value);
            break;

        // Notification channel toggles
        case 'channel-desktop':
            AppState.toggleNotificationChannel('desktop', value);
            render();
            break;
        case 'channel-mobile':
            AppState.toggleNotificationChannel('mobile', value);
            render();
            break;
        case 'channel-email':
            AppState.toggleNotificationChannel('email', value);
            render();
            break;
        case 'channel-slack':
            AppState.toggleNotificationChannel('slack', value);
            render();
            break;

        // Email digest toggles
        case 'sendImmediatelyOnUrgent':
            AppState.updateEmailDigestSetting('sendImmediatelyOnUrgent', value);
            break;
        case 'sendImmediatelyOnSLABreach':
            AppState.updateEmailDigestSetting('sendImmediatelyOnSLABreach', value);
            break;
        case 'delayLowPriorityToWorkHours':
            AppState.updateEmailDigestSetting('delayLowPriorityToWorkHours', value);
            break;

        // Communication preferences
        case 'changelog':
            AppState.updateCommunicationPreference('changelog', value);
            break;
        case 'dpaUpdates':
            AppState.updateCommunicationPreference('dpaUpdates', value);
            break;
        case 'productUpdates':
            AppState.updateCommunicationPreference('productUpdates', value);
            break;
        case 'tips':
            AppState.updateCommunicationPreference('tips', value);
            break;
    }
}

// ---- Action Handler ----

function handleAction(action, btn, e) {
    switch (action) {
        // ---- Profile Actions ----
        case 'save-name': {
            const name = document.getElementById('profileName')?.value?.trim();
            const username = document.getElementById('profileUsername')?.value?.trim();
            const errors = {};

            if (!name || name.length < 1) errors.name = 'Name is required';
            if (name && name.length > 128) errors.name = 'Name must be 128 characters or less';
            if (!username || username.length < 2) errors.username = 'Username must be at least 2 characters';
            if (username && !/^[a-zA-Z0-9][a-zA-Z0-9._-]*$/.test(username)) errors.username = 'Username must start with a letter or digit and contain only letters, digits, dots, dashes, or underscores';

            if (Object.keys(errors).length > 0) {
                AppState.validationErrors = errors;
                render();
                return;
            }

            AppState.validationErrors = {};
            AppState.updateProfile({ name, username });
            Components.showToast('Profile updated successfully', 'success');
            render();
            break;
        }

        case 'change-email': {
            Components.showModal('Change email address',
                `<div class="form-field">
                    <label class="form-label">New email address</label>
                    <input class="form-input" type="email" id="newEmail" data-testid="input-new-email" placeholder="Enter new email address" />
                    <div id="emailError" class="error-message" style="display:none"></div>
                </div>
                <div class="info-box" style="margin-top:12px"><span class="box-icon">&#8505;</span> A confirmation email will be sent to both old and new email addresses.</div>`,
                `<button class="btn btn-secondary" data-action="modal-cancel" data-testid="modal-cancel">Cancel</button>
                <button class="btn btn-primary" data-action="confirm-email-change" data-testid="modal-confirm">Change email</button>`
            );

            setTimeout(() => {
                document.querySelector('[data-action="modal-cancel"]').onclick = () => Components.closeModal();
                document.querySelector('[data-action="confirm-email-change"]').onclick = () => {
                    const email = document.getElementById('newEmail')?.value?.trim();
                    const errorEl = document.getElementById('emailError');
                    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                        errorEl.textContent = 'Please enter a valid email address';
                        errorEl.style.display = 'block';
                        return;
                    }
                    AppState.updateEmail(email);
                    Components.closeModal();
                    Components.showToast('Email address updated. Confirmation sent to both addresses.', 'success');
                    render();
                };
            }, 0);
            break;
        }

        case 'save-pronouns': {
            const pronouns = document.getElementById('profilePronouns')?.value?.trim() || '';
            AppState.updateProfile({ pronouns });
            Components.showToast('Pronouns updated', 'success');
            break;
        }

        case 'save-timezone': {
            const dd = document.getElementById('profileTimezone');
            const tz = dd?.getAttribute('data-value');
            if (tz) {
                AppState.updateProfile({ timezone: tz });
                Components.showToast('Timezone updated', 'success');
            }
            break;
        }

        case 'change-avatar': {
            Components.showToast('Avatar updated', 'success');
            break;
        }

        case 'disconnect-account': {
            const accountId = btn.getAttribute('data-account-id');
            const account = AppState.getConnectedAccountById(accountId);
            if (account) {
                Components.confirm(
                    'Disconnect account',
                    `Are you sure you want to disconnect your ${account.provider} account (${account.username})?`,
                    () => {
                        AppState.disconnectAccount(accountId);
                        Components.showToast(`${account.provider} account disconnected`, 'success');
                        render();
                    },
                    { danger: true, confirmText: 'Disconnect' }
                );
            }
            break;
        }

        case 'add-connected-account': {
            const availableProviders = ['GitHub', 'GitLab', 'Slack', 'Figma', 'Google', 'Bitbucket', 'Azure DevOps', 'Jira'];
            const existingProviders = new Set(AppState.connectedAccounts.map(a => a.provider));
            const unconnected = availableProviders.filter(p => !existingProviders.has(p));

            if (unconnected.length === 0) {
                Components.showToast('All available providers are already connected', 'info');
                return;
            }

            let optionsHtml = '<div class="provider-list" data-testid="provider-list">';
            for (const provider of unconnected) {
                optionsHtml += `<div class="provider-option" data-provider="${Components.escapeAttr(provider)}" data-testid="provider-${Components.escapeAttr(provider.toLowerCase().replace(/\s+/g, '-'))}">`;
                optionsHtml += `<span class="provider-icon">${Views._providerIcon(provider)}</span>`;
                optionsHtml += `<span>${Components.escapeHtml(provider)}</span>`;
                optionsHtml += `</div>`;
            }
            optionsHtml += '</div>';

            Components.showModal('Connect account', optionsHtml, '');

            setTimeout(() => {
                document.querySelectorAll('.provider-option').forEach(opt => {
                    opt.addEventListener('click', () => {
                        const provider = opt.getAttribute('data-provider');
                        const username = AppState.currentUser.username;
                        const email = AppState.currentUser.email;
                        AppState.addConnectedAccount({ provider, username, email });
                        Components.closeModal();
                        Components.showToast(`${provider} account connected`, 'success');
                        render();
                    });
                });
            }, 0);
            break;
        }

        case 'leave-workspace': {
            Components.confirm(
                'Leave workspace',
                `Are you sure you want to leave the ${AppState.workspace.name} workspace? You will lose access until an admin unsuspends your account.`,
                () => {
                    Components.showToast('You would be removed from the workspace', 'info');
                },
                { danger: true, confirmText: 'Leave workspace' }
            );
            break;
        }

        // ---- Preferences Actions ----
        // (Handled by toggle and dropdown handlers above)

        // ---- Notification Actions ----
        case 'unsubscribe': {
            const subId = btn.getAttribute('data-sub-id');
            AppState.removeSubscription(subId);
            Components.showToast('Unsubscribed from issue', 'success');
            render();
            break;
        }

        // ---- Security Actions ----
        case 'view-session': {
            const sessionId = btn.getAttribute('data-session-id');
            const session = AppState.getSessionById(sessionId);
            if (session) {
                const bodyHtml = `
                    <div class="detail-grid">
                        <div class="detail-row"><span class="detail-label">Device</span><span class="detail-value">${Components.escapeHtml(session.deviceName)}</span></div>
                        <div class="detail-row"><span class="detail-label">Source type</span><span class="detail-value">${Components.escapeHtml(session.sourceType)}</span></div>
                        <div class="detail-row"><span class="detail-label">Location</span><span class="detail-value">${Components.escapeHtml(session.location)}</span></div>
                        <div class="detail-row"><span class="detail-label">IP address</span><span class="detail-value"><code>${Components.escapeHtml(session.ipAddress)}</code></span></div>
                        <div class="detail-row"><span class="detail-label">Browser / Client</span><span class="detail-value">${Components.escapeHtml(session.browser)}</span></div>
                        <div class="detail-row"><span class="detail-label">Operating system</span><span class="detail-value">${Components.escapeHtml(session.os)}</span></div>
                        <div class="detail-row"><span class="detail-label">Signed in</span><span class="detail-value">${Components.formatDateTime(session.signedInAt)}</span></div>
                        <div class="detail-row"><span class="detail-label">Last seen</span><span class="detail-value">${Components.formatDateTime(session.lastSeenAt)}</span></div>
                        ${session.isCurrent ? '<div class="detail-row"><span class="detail-label">Status</span><span class="detail-value"><span class="current-badge">Current session</span></span></div>' : ''}
                    </div>
                `;
                Components.showModal('Session details', bodyHtml,
                    `<button class="btn btn-secondary" onclick="Components.closeModal()">Close</button>`
                );
            }
            break;
        }

        case 'revoke-session': {
            const sessionId = btn.getAttribute('data-session-id');
            const session = AppState.getSessionById(sessionId);
            if (session) {
                Components.confirm(
                    'Revoke session',
                    `Are you sure you want to revoke the session from ${session.deviceName}?`,
                    () => {
                        AppState.revokeSession(sessionId);
                        Components.showToast('Session revoked', 'success');
                        render();
                    },
                    { danger: true, confirmText: 'Revoke' }
                );
            }
            break;
        }

        case 'revoke-all-sessions': {
            Components.confirm(
                'Revoke all sessions',
                'Are you sure you want to revoke all sessions except the current one? You will be signed out from all other devices.',
                () => {
                    AppState.revokeAllSessionsExceptCurrent();
                    Components.showToast('All other sessions revoked', 'success');
                    render();
                },
                { danger: true, confirmText: 'Revoke all' }
            );
            break;
        }

        case 'add-passkey': {
            Components.showModal('Register passkey',
                `<div class="form-field">
                    <label class="form-label">Passkey name</label>
                    <input class="form-input" type="text" id="passkeyName" data-testid="input-passkey-name" placeholder="e.g., MacBook Pro Touch ID, 1Password" />
                    <div id="passkeyError" class="error-message" style="display:none"></div>
                </div>
                <div class="form-field">
                    <label class="form-label">Device type</label>
                </div>` +
                Components.dropdown('passkeyDeviceType', [
                    { id: 'platform', name: 'This device (platform authenticator)' },
                    { id: 'cross-platform', name: 'Security key or password manager' }
                ], 'cross-platform', {}),
                `<button class="btn btn-secondary" data-action="modal-cancel" data-testid="modal-cancel">Cancel</button>
                <button class="btn btn-primary" data-action="confirm-add-passkey" data-testid="modal-confirm">Register</button>`
            );

            setTimeout(() => {
                attachHandlers();
                document.querySelector('[data-action="modal-cancel"]').onclick = () => Components.closeModal();
                document.querySelector('[data-action="confirm-add-passkey"]').onclick = () => {
                    const name = document.getElementById('passkeyName')?.value?.trim();
                    const errorEl = document.getElementById('passkeyError');
                    if (!name || name.length < 2) {
                        errorEl.textContent = 'Please enter a name for the passkey (at least 2 characters)';
                        errorEl.style.display = 'block';
                        return;
                    }
                    const deviceTypeDd = document.getElementById('passkeyDeviceType');
                    const deviceType = deviceTypeDd?.getAttribute('data-value') || 'cross-platform';
                    AppState.addPasskey({ name, deviceType });
                    Components.closeModal();
                    Components.showToast('Passkey registered', 'success');
                    render();
                };
            }, 0);
            break;
        }

        case 'rename-passkey': {
            const pkId = btn.getAttribute('data-passkey-id');
            const pk = AppState.getPasskeyById(pkId);
            if (pk) {
                Components.showModal('Rename passkey',
                    `<div class="form-field">
                        <label class="form-label">New name</label>
                        <input class="form-input" type="text" id="passkeyNewName" data-testid="input-passkey-new-name" value="${Components.escapeAttr(pk.name)}" />
                        <div id="passkeyRenameError" class="error-message" style="display:none"></div>
                    </div>`,
                    `<button class="btn btn-secondary" data-action="modal-cancel" data-testid="modal-cancel">Cancel</button>
                    <button class="btn btn-primary" data-action="confirm-rename-passkey" data-testid="modal-confirm">Save</button>`
                );
                setTimeout(() => {
                    document.querySelector('[data-action="modal-cancel"]').onclick = () => Components.closeModal();
                    document.querySelector('[data-action="confirm-rename-passkey"]').onclick = () => {
                        const newName = document.getElementById('passkeyNewName')?.value?.trim();
                        if (!newName || newName.length < 2) {
                            document.getElementById('passkeyRenameError').textContent = 'Name must be at least 2 characters';
                            document.getElementById('passkeyRenameError').style.display = 'block';
                            return;
                        }
                        AppState.renamePasskey(pkId, newName);
                        Components.closeModal();
                        Components.showToast('Passkey renamed', 'success');
                        render();
                    };
                }, 0);
            }
            break;
        }

        case 'remove-passkey': {
            const pkId = btn.getAttribute('data-passkey-id');
            const pk = AppState.getPasskeyById(pkId);
            if (pk) {
                Components.confirm(
                    'Remove passkey',
                    `Are you sure you want to remove the passkey "${pk.name}"?`,
                    () => {
                        AppState.removePasskey(pkId);
                        Components.showToast('Passkey removed', 'success');
                        render();
                    },
                    { danger: true, confirmText: 'Remove' }
                );
            }
            break;
        }

        case 'create-api-key': {
            Components.showModal('Create API key',
                `<div class="form-field">
                    <label class="form-label">Label</label>
                    <input class="form-input" type="text" id="apiKeyLabel" data-testid="input-api-key-label" placeholder="e.g., CI/CD Pipeline, Personal Automation" />
                    <div id="apiKeyError" class="error-message" style="display:none"></div>
                </div>`,
                `<button class="btn btn-secondary" data-action="modal-cancel" data-testid="modal-cancel">Cancel</button>
                <button class="btn btn-primary" data-action="confirm-create-api-key" data-testid="modal-confirm">Create</button>`
            );

            setTimeout(() => {
                document.querySelector('[data-action="modal-cancel"]').onclick = () => Components.closeModal();
                document.querySelector('[data-action="confirm-create-api-key"]').onclick = () => {
                    const label = document.getElementById('apiKeyLabel')?.value?.trim();
                    const errorEl = document.getElementById('apiKeyError');
                    if (!label || label.length < 2) {
                        errorEl.textContent = 'Please enter a label for the API key (at least 2 characters)';
                        errorEl.style.display = 'block';
                        return;
                    }
                    AppState.createApiKey(label);
                    Components.closeModal();
                    Components.showToast('API key created', 'success');
                    render();
                };
            }, 0);
            break;
        }

        case 'rename-api-key': {
            const keyId = btn.getAttribute('data-key-id');
            const key = AppState.getApiKeyById(keyId);
            if (key) {
                Components.showModal('Rename API key',
                    `<div class="form-field">
                        <label class="form-label">New label</label>
                        <input class="form-input" type="text" id="apiKeyNewLabel" data-testid="input-api-key-new-label" value="${Components.escapeAttr(key.label)}" />
                        <div id="apiKeyRenameError" class="error-message" style="display:none"></div>
                    </div>`,
                    `<button class="btn btn-secondary" data-action="modal-cancel" data-testid="modal-cancel">Cancel</button>
                    <button class="btn btn-primary" data-action="confirm-rename-api-key" data-testid="modal-confirm">Save</button>`
                );
                setTimeout(() => {
                    document.querySelector('[data-action="modal-cancel"]').onclick = () => Components.closeModal();
                    document.querySelector('[data-action="confirm-rename-api-key"]').onclick = () => {
                        const newLabel = document.getElementById('apiKeyNewLabel')?.value?.trim();
                        if (!newLabel || newLabel.length < 2) {
                            document.getElementById('apiKeyRenameError').textContent = 'Label must be at least 2 characters';
                            document.getElementById('apiKeyRenameError').style.display = 'block';
                            return;
                        }
                        AppState.renameApiKey(keyId, newLabel);
                        Components.closeModal();
                        Components.showToast('API key renamed', 'success');
                        render();
                    };
                }, 0);
            }
            break;
        }

        case 'revoke-api-key': {
            const keyId = btn.getAttribute('data-key-id');
            const key = AppState.getApiKeyById(keyId);
            if (key) {
                Components.confirm(
                    'Revoke API key',
                    `Are you sure you want to revoke the API key "${key.label}"? This action cannot be undone.`,
                    () => {
                        AppState.revokeApiKey(keyId);
                        Components.showToast('API key revoked', 'success');
                        render();
                    },
                    { danger: true, confirmText: 'Revoke' }
                );
            }
            break;
        }

        case 'revoke-app': {
            const appId = btn.getAttribute('data-app-id');
            const app = AppState.getAuthorizedAppById(appId);
            if (app) {
                Components.confirm(
                    'Revoke application access',
                    `Are you sure you want to revoke access for ${app.name}? This will disconnect the integration.`,
                    () => {
                        AppState.revokeAuthorizedApp(appId);
                        Components.showToast(`${app.name} access revoked`, 'success');
                        render();
                    },
                    { danger: true, confirmText: 'Revoke access' }
                );
            }
            break;
        }

        // ---- Reset Data ----
        case 'reset-data': {
            Components.confirm(
                'Reset to defaults',
                'This will reset all settings to their default values. This action cannot be undone.',
                () => {
                    AppState.resetToSeedData();
                    Components.showToast('All settings reset to defaults', 'success');
                    navigate('/profile');
                },
                { danger: true, confirmText: 'Reset' }
            );
            break;
        }
    }
}

// ---- SSE Connection ----

function _connectSSE() {
    const eventSource = new EventSource('/api/events');
    eventSource.onmessage = (e) => {
        if (e.data === 'reset') {
            AppState.resetToSeedData();
            navigate('/profile');
        }
    };
    eventSource.onerror = () => {
        // Silently reconnect
    };
}

// ---- Initialize ----

function initApp() {
    // Parse initial route from hash
    const hash = window.location.hash.replace('#', '') || '/profile';
    AppState.currentRoute = ROUTES[hash] ? hash : '/profile';

    // Handle browser navigation
    window.addEventListener('hashchange', () => {
        const newHash = window.location.hash.replace('#', '') || '/profile';
        if (ROUTES[newHash] && newHash !== AppState.currentRoute) {
            AppState.currentRoute = newHash;
            render();
        }
    });

    // Modal close button
    document.getElementById('modalClose')?.addEventListener('click', () => {
        Components.closeModal();
    });

    // Close modal on overlay click
    document.getElementById('modalOverlay')?.addEventListener('click', (e) => {
        if (e.target === e.currentTarget) {
            Components.closeModal();
        }
    });

    // SSE
    _connectSSE();

    // Initial render
    render();
}

// Start the app
document.addEventListener('DOMContentLoaded', initApp);
