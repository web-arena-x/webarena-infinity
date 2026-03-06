/* ============================================================
   Elation Patient Communication — App Controller
   ============================================================ */

const App = {
    _previousView: null,

    // ── Routing ─────────────────────────────────────────────
    parseRoute() {
        const hash = window.location.hash.replace('#/', '') || 'home';
        const parts = hash.split('/');
        const view = parts[0];

        this._previousView = AppState.currentView;

        switch (view) {
            case 'home':
                AppState.currentView = 'home';
                break;
            case 'inbox':
                AppState.currentView = 'inbox';
                break;
            case 'sent':
                AppState.currentView = 'sent';
                break;
            case 'drafts':
                AppState.currentView = 'drafts';
                break;
            case 'reminders':
                AppState.currentView = 'reminders';
                break;
            case 'patients':
                AppState.currentView = 'patients';
                AppState.currentPatientId = null;
                break;
            case 'patient':
                AppState.currentView = 'patient-detail';
                AppState.currentPatientId = parts[1] || null;
                break;
            case 'conversation':
                AppState.currentView = 'conversation';
                AppState.currentConversationId = parts[1] || null;
                AppState.currentPatientId = parts[2] || null;
                break;
            case 'appointments':
                AppState.currentView = 'appointments';
                break;
            case 'bulk-letters':
                AppState.currentView = 'bulk-letters';
                break;
            case 'settings':
                AppState.currentView = 'settings';
                if (parts[1]) AppState.settingsTab = parts[1];
                break;
            default:
                AppState.currentView = 'home';
        }
    },

    navigate(route) {
        window.location.hash = '#/' + route;
    },

    // ── Render ──────────────────────────────────────────────
    render() {
        const sidebar = document.getElementById('sidebarNav');
        const content = document.getElementById('contentWrapper');

        sidebar.innerHTML = Views.renderSidebar();

        // Update user info in topbar
        const userAvatar = document.getElementById('userAvatar');
        if (userAvatar) {
            userAvatar.innerHTML = Components.avatar(
                `${AppState.currentUser.firstName} ${AppState.currentUser.lastName}`,
                AppState.currentUser.avatarColor, 32
            );
        }
        const userName = document.getElementById('userName');
        if (userName) {
            userName.textContent = `Dr. ${AppState.currentUser.lastName}`;
        }

        let html = '';
        switch (AppState.currentView) {
            case 'home':
                html = Views.renderHome();
                break;
            case 'inbox':
                html = Views.renderInbox();
                break;
            case 'sent':
                html = Views.renderSent();
                break;
            case 'drafts':
                html = Views.renderDrafts();
                break;
            case 'reminders':
                html = Views.renderReminders();
                break;
            case 'patients':
                html = Views.renderPatients();
                break;
            case 'patient-detail':
                html = Views.renderPatientDetail(AppState.currentPatientId);
                break;
            case 'conversation':
                html = Views.renderConversation(AppState.currentConversationId, AppState.currentPatientId);
                break;
            case 'appointments':
                html = Views.renderAppointments();
                break;
            case 'bulk-letters':
                html = Views.renderBulkLetters();
                break;
            case 'settings':
                html = Views.renderSettings();
                break;
            default:
                html = Views.renderHome();
        }

        content.innerHTML = html;

        // Render compose overlay if open
        this._renderComposeOverlay();

        // Re-attach dynamic listeners
        this._attachDynamicListeners();
    },

    _renderComposeOverlay() {
        const overlay = document.getElementById('composeOverlay');
        if (AppState.composeOpen) {
            overlay.innerHTML = Views.renderComposeModal(
                AppState.composeDraft?.patientId,
                AppState.composeDraft || {}
            );
            overlay.style.display = 'block';
        } else {
            overlay.style.display = 'none';
        }
    },

    _attachDynamicListeners() {
        // Patient search in compose
        const composeTo = document.getElementById('composeTo');
        if (composeTo) {
            composeTo.addEventListener('input', (e) => this._handlePatientSearch(e.target.value, 'patientSuggestions', 'composePatientId'));
        }

        // Appointment patient search
        const apptSearch = document.getElementById('apptPatientSearch');
        if (apptSearch) {
            apptSearch.addEventListener('input', (e) => this._handlePatientSearch(e.target.value, 'apptPatientSuggestions', 'apptPatientId'));
        }

        // Patient list search
        const patientSearch = document.getElementById('patientSearch');
        if (patientSearch) {
            patientSearch.addEventListener('input', (e) => {
                AppState.patientListFilter.search = e.target.value;
                AppState.patientListPage = 1;
                this.render();
                // Re-focus and set cursor position
                const input = document.getElementById('patientSearch');
                if (input) {
                    input.focus();
                    input.setSelectionRange(input.value.length, input.value.length);
                }
            });
        }
    },

    _handlePatientSearch(query, suggestionsId, hiddenId) {
        const container = document.getElementById(suggestionsId);
        if (!container) return;
        if (!query || query.length < 2) {
            container.innerHTML = '';
            container.style.display = 'none';
            return;
        }
        const results = AppState.searchPatients(query);
        if (results.length === 0) {
            container.innerHTML = '<div class="suggestion-empty">No patients found</div>';
            container.style.display = 'block';
            return;
        }
        container.innerHTML = results.map(p =>
            `<div class="suggestion-item" data-action="select-patient-suggestion" data-patient="${p.id}" data-hidden="${hiddenId}">${Components.escapeHtml(p.firstName)} ${Components.escapeHtml(p.lastName)} <span class="suggestion-email">${Components.escapeHtml(p.email || '')}</span></div>`
        ).join('');
        container.style.display = 'block';
    },

    // ── Event Handling ──────────────────────────────────────
    handleClick(e) {
        const target = e.target;

        // Close dropdowns when clicking outside
        if (!target.closest('.custom-dropdown')) {
            document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
        }

        // Close suggestion dropdowns
        if (!target.closest('.suggestions-dropdown') && !target.closest('.form-input')) {
            document.querySelectorAll('.suggestions-dropdown').forEach(d => { d.style.display = 'none'; });
        }

        // Route navigation
        const routeEl = target.closest('[data-route]');
        if (routeEl) {
            e.preventDefault();
            App.navigate(routeEl.dataset.route);
            return;
        }

        // Dropdown item selection (must be checked before dropdown trigger)
        const ddItem = target.closest('.dropdown-item[data-value]');
        if (ddItem) {
            const ddId = ddItem.dataset.dropdownId;
            const value = ddItem.dataset.value;
            App.handleDropdownSelect(ddId, value);
            // Close menu
            ddItem.closest('.dropdown-menu')?.classList.remove('open');
            return;
        }

        // Dropdown trigger
        const ddTrigger = target.closest('[data-dropdown]');
        if (ddTrigger) {
            const ddId = ddTrigger.dataset.dropdown;
            const menu = document.getElementById(ddId + '-menu');
            if (menu) {
                const wasOpen = menu.classList.contains('open');
                document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
                if (!wasOpen) menu.classList.add('open');
            }
            return;
        }

        // Settings tab
        const settingsTab = target.closest('[data-settings-tab]');
        if (settingsTab) {
            AppState.settingsTab = settingsTab.dataset.settingsTab;
            App.navigate('settings/' + AppState.settingsTab);
            return;
        }

        // Toggle switch
        const toggleInput = target.closest('.toggle-switch input');
        if (toggleInput) {
            App.handleToggle(toggleInput.dataset.toggle || toggleInput.id, toggleInput.checked);
            return;
        }

        // Checkbox
        const checkboxInput = target.closest('[data-checkbox]');
        if (checkboxInput) {
            App.handleCheckbox(checkboxInput.dataset.checkbox, checkboxInput.checked);
            return;
        }

        // Patient checkbox in table
        const patientSelect = target.closest('[data-patient-select]');
        if (patientSelect) {
            const patId = patientSelect.dataset.patientSelect;
            if (patientSelect.checked) {
                if (!AppState.selectedPatientIds.includes(patId)) {
                    AppState.selectedPatientIds.push(patId);
                }
            } else {
                AppState.selectedPatientIds = AppState.selectedPatientIds.filter(id => id !== patId);
            }
            App.render();
            return;
        }

        // Action dispatch
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            e.preventDefault();
            App.handleAction(actionEl.dataset.action, actionEl);
            return;
        }

        // Modal overlay click to close
        if (target.id === 'modalOverlay') {
            Components.closeModal();
            return;
        }
    },

    // ── Action Handler ──────────────────────────────────────
    handleAction(action, el) {
        switch (action) {
            // Navigation
            case 'go-back':
                window.history.back();
                break;

            case 'open-patient':
                App.navigate('patient/' + el.dataset.patient);
                break;

            case 'open-conversation':
                App.navigate('conversation/' + el.dataset.conversation + '/' + el.dataset.patient);
                break;

            // Compose
            case 'compose-letter':
                AppState.composeOpen = true;
                AppState.composeDraft = {};
                App.render();
                break;

            case 'compose-to-patient':
                AppState.composeOpen = true;
                AppState.composeDraft = { patientId: el.dataset.patient };
                App.render();
                break;

            case 'close-compose':
                AppState.composeOpen = false;
                AppState.composeDraft = null;
                App.render();
                break;

            case 'select-patient-suggestion': {
                const patId = el.dataset.patient;
                const patient = AppState.getPatient(patId);
                const hiddenId = el.dataset.hidden;
                if (patient && hiddenId) {
                    const hidden = document.getElementById(hiddenId);
                    if (hidden) hidden.value = patId;
                    // Update compose
                    if (hiddenId === 'composePatientId') {
                        AppState.composeDraft = AppState.composeDraft || {};
                        AppState.composeDraft.patientId = patId;
                        App._renderComposeOverlay();
                    }
                    // Update appointment
                    const searchInput = hiddenId === 'composePatientId'
                        ? document.getElementById('composeTo')
                        : document.getElementById('apptPatientSearch');
                    if (searchInput) {
                        searchInput.value = `${patient.firstName} ${patient.lastName}`;
                    }
                }
                document.querySelectorAll('.suggestions-dropdown').forEach(d => { d.style.display = 'none'; });
                break;
            }

            case 'send-composed-letter': {
                const patientId = document.getElementById('composePatientId')?.value;
                const subject = document.getElementById('composeSubject')?.value;
                const body = document.getElementById('composeBody')?.value;
                const unreadAlert = this._getDropdownValue('composeUnreadAlert');
                const noReply = document.getElementById('composeNoReply')?.checked;

                if (!patientId || !subject || !body) {
                    Components.showToast('Please fill in all required fields.', 'error');
                    return;
                }
                AppState.sendLetter(patientId, subject, body, {
                    unreadAlertTimeframe: unreadAlert,
                    doNotAllowResponse: noReply
                });
                AppState.composeOpen = false;
                AppState.composeDraft = null;
                Components.showToast('Letter sent successfully.', 'success');
                App.render();
                break;
            }

            case 'save-as-draft': {
                const patientId = document.getElementById('composePatientId')?.value;
                const subject = document.getElementById('composeSubject')?.value;
                const body = document.getElementById('composeBody')?.value;
                if (!patientId) {
                    Components.showToast('Please select a patient.', 'error');
                    return;
                }
                AppState.saveDraft(patientId, subject || '', body || '');
                AppState.composeOpen = false;
                AppState.composeDraft = null;
                Components.showToast('Draft saved.', 'success');
                App.render();
                break;
            }

            case 'edit-draft': {
                const letter = AppState.patientLetters.find(l => l.id === el.dataset.letter);
                if (letter) {
                    AppState.composeOpen = true;
                    AppState.composeDraft = {
                        patientId: letter.patientId,
                        subject: letter.subject,
                        body: letter.body,
                        letterId: letter.id,
                        draft: true,
                        doNotAllowResponse: letter.doNotAllowResponse,
                        unreadAlertTimeframe: letter.unreadAlertTimeframe
                    };
                    App.render();
                }
                break;
            }

            case 'send-draft': {
                AppState.sendDraft(el.dataset.letter);
                AppState.composeOpen = false;
                AppState.composeDraft = null;
                Components.showToast('Letter sent.', 'success');
                App.render();
                break;
            }

            case 'update-draft': {
                const subject = document.getElementById('composeSubject')?.value;
                const body = document.getElementById('composeBody')?.value;
                const noReply = document.getElementById('composeNoReply')?.checked;
                AppState.saveDraft(null, subject, body, {
                    letterId: el.dataset.letter,
                    doNotAllowResponse: noReply
                });
                AppState.composeOpen = false;
                AppState.composeDraft = null;
                Components.showToast('Draft updated.', 'success');
                App.render();
                break;
            }

            case 'delete-draft':
                Components.confirm('Delete Draft', 'Are you sure you want to delete this draft?', () => {
                    AppState.deleteDraft(el.dataset.letter);
                    Components.closeModal();
                    Components.showToast('Draft deleted.', 'success');
                    App.render();
                });
                break;

            // Conversation
            case 'send-reply': {
                const body = document.getElementById('replyBody')?.value;
                if (!body || !body.trim()) {
                    Components.showToast('Please enter a reply.', 'error');
                    return;
                }
                AppState.replyToConversation(el.dataset.conversation, body.trim());
                Components.showToast('Reply sent.', 'success');
                App.render();
                break;
            }

            case 'sign-off-conversation':
                Components.confirm('End Conversation', 'Are you sure you want to sign off and end this conversation? The patient will not be able to reply.', () => {
                    AppState.endConversation(el.dataset.conversation);
                    Components.closeModal();
                    Components.showToast('Conversation ended.', 'success');
                    App.render();
                });
                break;

            // Passport
            case 'open-passport-dialog':
                Components.showModal('Passport Settings', Views.renderPassportDialog(el.dataset.patient), '');
                break;

            case 'send-passport-invite':
            case 'confirm-send-invite': {
                const patId = el.dataset.patient;
                const email = document.getElementById('passportEmail')?.value;
                const phone = document.getElementById('passportPhone')?.value;
                const sharingLevel = this._getDropdownValue('passportSharingLevel');
                if (!email) {
                    Components.showToast('Email address is required for Passport invitation.', 'error');
                    return;
                }
                AppState.sendPassportInvitation(patId, {
                    email,
                    cellPhone: phone,
                    sharingLevel: sharingLevel ? parseInt(sharingLevel) : undefined
                });
                Components.closeModal();
                Components.showToast('Passport invitation sent.', 'success');
                App.render();
                break;
            }

            case 'resend-passport-invite':
                AppState.resendPassportInvitation(el.dataset.patient);
                Components.showToast('Passport invitation re-sent.', 'success');
                App.render();
                break;

            case 'confirm-save-passport': {
                const patId = el.dataset.patient;
                const email = document.getElementById('passportEmail')?.value;
                const phone = document.getElementById('passportPhone')?.value;
                const sharingLevel = this._getDropdownValue('passportSharingLevel');
                AppState.updatePatientDemographics(patId, { email, cellPhone: phone });
                if (sharingLevel) AppState.updatePassportSharingLevel(patId, parseInt(sharingLevel));
                Components.closeModal();
                Components.showToast('Passport settings saved.', 'success');
                App.render();
                break;
            }

            case 'view-invitation-code': {
                const patient = AppState.getPatient(el.dataset.patient);
                if (patient && patient.invitationCode) {
                    Components.showModal('Invitation Code',
                        `<p>Invitation code for ${Components.escapeHtml(patient.firstName)} ${Components.escapeHtml(patient.lastName)}:</p><div class="invitation-code-large" data-testid="invitation-code-display">${patient.invitationCode}</div>`,
                        '<button class="btn btn-secondary" data-action="close-modal">Dismiss</button>'
                    );
                }
                break;
            }

            case 'disable-passport':
                Components.confirmDanger('Disable Passport', 'Are you sure you want to disable this patient\'s Passport account? They will lose access to their portal.', () => {
                    AppState.disablePassportAccount(el.dataset.patient);
                    Components.closeModal();
                    Components.showToast('Passport account disabled.', 'success');
                    App.render();
                });
                break;

            // Tags
            case 'add-tag':
                Components.showModal('Add Tag', Views.renderAddTagModal(el.dataset.patient), '');
                break;

            case 'confirm-add-tag':
                AppState.addPatientTag(el.dataset.patient, el.dataset.tag);
                Components.closeModal();
                App.render();
                break;

            case 'remove-tag':
                AppState.removePatientTag(el.dataset.patient, el.dataset.tag);
                App.render();
                break;

            // SMS
            case 'request-sms-optin': {
                const patient = AppState.getPatient(el.dataset.patient);
                if (patient) {
                    Components.showToast(`SMS opt-in request sent to ${patient.firstName} ${patient.lastName}.`, 'success');
                }
                break;
            }
            case 'opt-out-sms': {
                const patient = AppState.getPatient(el.dataset.patient);
                if (patient) {
                    AppState.updatePatientDemographics(el.dataset.patient, { smsOptInStatus: 'opted_out' });
                    Components.showToast(`${patient.firstName} ${patient.lastName} has been opted out of SMS.`, 'success');
                    App.render();
                }
                break;
            }

            // Emergency Contact
            case 'edit-emergency-contact':
                Components.showModal('Emergency Contact', Views.renderEmergencyContactModal(el.dataset.patient), '');
                break;
            case 'save-emergency-contact': {
                const ecName = document.getElementById('ec-name')?.value?.trim();
                const ecPhone = document.getElementById('ec-phone')?.value?.trim();
                const ecRelationship = document.getElementById('ec-relationship')?.value?.trim();
                if (!ecName || !ecPhone || !ecRelationship) {
                    Components.showToast('Please fill in all emergency contact fields.', 'error');
                    break;
                }
                AppState.updatePatientDemographics(el.dataset.patient, {
                    emergencyContact: { name: ecName, phone: ecPhone, relationship: ecRelationship }
                });
                Components.closeModal();
                Components.showToast('Emergency contact saved.', 'success');
                App.render();
                break;
            }

            // Reminders
            case 'acknowledge-reminder':
                AppState.acknowledgeReminder(el.dataset.reminder);
                App.render();
                break;

            case 'reminder-resend': {
                const rem = AppState.reminders.find(r => r.id === el.dataset.reminder);
                if (rem && rem.patientLetterId) {
                    const letter = AppState.patientLetters.find(l => l.id === rem.patientLetterId);
                    if (letter) {
                        Components.showToast('Letter re-sent to patient.', 'success');
                    }
                }
                AppState.acknowledgeReminder(el.dataset.reminder);
                App.render();
                break;
            }

            case 'reminder-write':
                AppState.composeOpen = true;
                AppState.composeDraft = { patientId: el.dataset.patient };
                AppState.acknowledgeReminder(el.dataset.reminder);
                App.render();
                break;

            // Patients
            case 'select-all-patients': {
                const allOnPage = AppState.getPagedPatients().patients.map(p => p.id);
                const allSelected = allOnPage.every(id => AppState.selectedPatientIds.includes(id));
                if (allSelected) {
                    AppState.selectedPatientIds = AppState.selectedPatientIds.filter(id => !allOnPage.includes(id));
                } else {
                    for (const id of allOnPage) {
                        if (!AppState.selectedPatientIds.includes(id)) {
                            AppState.selectedPatientIds.push(id);
                        }
                    }
                }
                App.render();
                break;
            }

            case 'prev-page':
                if (AppState.patientListPage > 1) {
                    AppState.patientListPage--;
                    App.render();
                }
                break;

            case 'next-page': {
                const totalPages = AppState.getPagedPatients().totalPages;
                if (AppState.patientListPage < totalPages) {
                    AppState.patientListPage++;
                    App.render();
                }
                break;
            }

            case 'bulk-send-letter':
                Components.showModal('Send Bulk Letter', Views.renderBulkComposeModal(), '');
                break;

            case 'bulk-invite-passport': {
                const uninvited = AppState.selectedPatientIds.filter(id => {
                    const p = AppState.getPatient(id);
                    return p && p.passportStatus === 'not_invited' && p.email;
                });
                if (uninvited.length === 0) {
                    Components.showToast('No eligible patients selected (must be uninvited with email).', 'error');
                    return;
                }
                Components.confirm('Send Passport Invitations', `Send Passport invitations to ${uninvited.length} patient(s)?`, () => {
                    for (const id of uninvited) {
                        AppState.sendPassportInvitation(id, {});
                    }
                    AppState.selectedPatientIds = [];
                    Components.closeModal();
                    Components.showToast(`Invitations sent to ${uninvited.length} patients.`, 'success');
                    App.render();
                });
                break;
            }

            case 'confirm-send-bulk': {
                const desc = document.getElementById('bulkDescription')?.value;
                const subject = document.getElementById('bulkSubject')?.value;
                const body = document.getElementById('bulkBody')?.value;
                const allowResp = document.getElementById('bulkAllowResponse')?.checked;
                if (!desc || !subject || !body) {
                    Components.showToast('Please fill in all required fields.', 'error');
                    return;
                }
                AppState.sendBulkLetter({
                    description: desc,
                    subject,
                    body,
                    allowResponse: allowResp,
                    targetPatientIds: AppState.selectedPatientIds
                });
                AppState.selectedPatientIds = [];
                Components.closeModal();
                Components.showToast('Bulk letter sent.', 'success');
                App.render();
                break;
            }

            // Appointments
            case 'new-appointment':
                Components.showModal('New Appointment', Views.renderNewAppointmentModal(), '');
                break;

            case 'confirm-new-appointment': {
                const patId = document.getElementById('apptPatientId')?.value;
                const date = document.getElementById('apptDate')?.value;
                const time = document.getElementById('apptTime')?.value;
                const provider = this._getDropdownValue('apptProvider');
                const place = this._getDropdownValue('apptPlace');
                const reason = document.getElementById('apptReason')?.value;
                if (!patId || !date || !time) {
                    Components.showToast('Please fill in patient, date, and time.', 'error');
                    return;
                }
                const dateTime = `${date}T${time}:00Z`;
                const prov = AppState.providers.find(p => p.id === provider);
                let virtualInstr = null;
                if (place === 'virtual' && prov && prov.virtualVisitActivated) {
                    virtualInstr = prov.virtualVisitInstructions;
                }
                AppState.addAppointment({
                    patientId: patId,
                    providerId: provider || AppState.currentUser.id,
                    date: dateTime,
                    place: place || 'in_person',
                    status: 'scheduled',
                    virtualVisitInstructions: virtualInstr,
                    reason: reason || ''
                });
                Components.closeModal();
                Components.showToast('Appointment scheduled.', 'success');
                App.render();
                break;
            }

            case 'cancel-appointment':
                Components.confirm('Cancel Appointment', 'Are you sure you want to cancel this appointment?', () => {
                    AppState.cancelAppointment(el.dataset.appointment);
                    Components.closeModal();
                    Components.showToast('Appointment cancelled.', 'success');
                    App.render();
                });
                break;

            case 'start-video': {
                const appt = AppState.appointments.find(a => a.id === el.dataset.appointment);
                if (appt && appt.virtualVisitInstructions) {
                    Components.showModal('Virtual Visit', `<p>Starting virtual visit...</p><p>Video link: <strong>${Components.escapeHtml(appt.virtualVisitInstructions)}</strong></p><p>The patient will be in the waiting room. Click Admit when ready.</p>`, '<button class="btn btn-primary" data-action="close-modal">Close</button>');
                } else {
                    Components.showToast('No video link configured for this appointment.', 'error');
                }
                break;
            }

            // Settings
            case 'save-user-settings': {
                const sharingDefault = this._getDropdownValue('sharingDefault');
                const notifTimeframe = this._getDropdownValue('notificationTimeframe');
                AppState.updateProviderSettings(AppState.currentUser.id, {
                    sharingDefault: sharingDefault ? parseInt(sharingDefault) : undefined,
                    notificationTimeframe: notifTimeframe || undefined
                });
                Components.showToast('Settings saved.', 'success');
                App.render();
                break;
            }

            case 'save-admin-settings': {
                const allowMsg = document.getElementById('allowPatientMessaging')?.checked;
                const autoInvite = document.getElementById('bookingSiteAutoInvite')?.checked;
                AppState.updatePracticeSettings({
                    allowPatientMessaging: allowMsg,
                    bookingSiteAutoInvite: autoInvite
                });
                Components.showToast('Admin settings saved.', 'success');
                App.render();
                break;
            }

            case 'save-telehealth-settings': {
                const screenSharing = document.getElementById('screenSharingPatients')?.checked;
                const chatMode = this._getDropdownValue('chatMode');
                const audioNotif = document.getElementById('waitingRoomAudioNotification')?.checked;
                AppState.updateVideoSettings({
                    screenSharingPatients: screenSharing,
                    chatMode: chatMode || 'everyone_in_meeting',
                    waitingRoomAudioNotification: audioNotif
                });
                Components.showToast('Telehealth settings saved.', 'success');
                App.render();
                break;
            }

            // Routing
            case 'add-routing-recipient':
                Components.showModal('Add Recipient', Views.renderAddRoutingRecipientModal(el.dataset.provider, el.dataset.category), '');
                break;

            case 'confirm-add-routing': {
                const provId = el.dataset.provider;
                const category = el.dataset.category;
                const recipientId = el.dataset.recipient;
                const current = (AppState.messageRouting[provId] || {})[category] || [];
                if (!current.includes(recipientId)) {
                    current.push(recipientId);
                    AppState.updateMessageRouting(provId, category, current);
                }
                Components.showModal('Add Recipient', Views.renderAddRoutingRecipientModal(provId, category), '');
                break;
            }

            case 'remove-routing-recipient': {
                const provId = el.dataset.provider;
                const category = el.dataset.category;
                const recipientId = el.dataset.recipient;
                const current = (AppState.messageRouting[provId] || {})[category] || [];
                AppState.updateMessageRouting(provId, category, current.filter(r => r !== recipientId));
                App.render();
                break;
            }

            case 'update-all-routing':
                Components.confirm('Update All Providers', 'Apply the current provider\'s routing to all providers?', () => {
                    const selectedProvId = AppState._routingSelectedProvider || AppState.currentUser.id;
                    const provRouting = AppState.messageRouting[selectedProvId] || {};
                    for (const cat of AppState.messageCategories) {
                        const recipients = provRouting[cat] || [];
                        AppState.updateAllProvidersRouting(cat, recipients);
                    }
                    Components.closeModal();
                    Components.showToast('Routing updated for all providers.', 'success');
                    App.render();
                });
                break;

            // Telehealth
            case 'activate-telehealth':
                Components.showModal('Activate Virtual Visit', Views.renderTelehealthInstructionsModal(el.dataset.provider), '');
                break;

            case 'deactivate-telehealth':
                Components.confirmDanger('Deactivate Virtual Visit', 'Are you sure you want to deactivate virtual visits for this provider?', () => {
                    AppState.deactivateVirtualVisit(el.dataset.provider);
                    Components.closeModal();
                    Components.showToast('Virtual visits deactivated.', 'success');
                    App.render();
                });
                break;

            case 'edit-telehealth-instructions':
                Components.showModal('Edit Instructions', Views.renderTelehealthInstructionsModal(el.dataset.provider), '');
                break;

            case 'confirm-edit-instructions': {
                const instructions = document.getElementById('telehealthInstructions')?.value;
                const provId = el.dataset.provider;
                const prov = AppState.providers.find(p => p.id === provId);
                if (prov && !prov.virtualVisitActivated) {
                    AppState.activateVirtualVisit(provId, instructions);
                } else {
                    AppState.updateVirtualVisitInstructions(provId, instructions);
                }
                Components.closeModal();
                Components.showToast('Instructions saved.', 'success');
                App.render();
                break;
            }

            // Practice Locations
            case 'add-location':
                Components.showModal('Add Location', Views.renderLocationModal(), '');
                break;

            case 'edit-location': {
                const loc = AppState.practiceSettings.practiceLocations.find(l => l.id === el.dataset.location);
                if (loc) Components.showModal('Edit Location', Views.renderLocationModal(loc), '');
                break;
            }

            case 'confirm-add-location': {
                const name = document.getElementById('locName')?.value;
                const address = document.getElementById('locAddress')?.value;
                const posCode = document.getElementById('locPosCode')?.value;
                const posDesc = document.getElementById('locPosDesc')?.value;
                if (!name || !address || !posCode) {
                    Components.showToast('Please fill in all required fields.', 'error');
                    return;
                }
                AppState.addPracticeLocation({ name, address, posCode, posDescription: posDesc || '' });
                Components.closeModal();
                Components.showToast('Location added.', 'success');
                App.render();
                break;
            }

            case 'confirm-edit-location': {
                const locId = el.dataset.location;
                const name = document.getElementById('locName')?.value;
                const address = document.getElementById('locAddress')?.value;
                const posCode = document.getElementById('locPosCode')?.value;
                const posDesc = document.getElementById('locPosDesc')?.value;
                if (!name || !address || !posCode) {
                    Components.showToast('Please fill in all required fields.', 'error');
                    return;
                }
                AppState.updatePracticeLocation(locId, { name, address, posCode, posDescription: posDesc || '' });
                Components.closeModal();
                Components.showToast('Location updated.', 'success');
                App.render();
                break;
            }

            case 'remove-location':
                Components.confirmDanger('Remove Location', 'Are you sure you want to remove this practice location?', () => {
                    AppState.removePracticeLocation(el.dataset.location);
                    Components.closeModal();
                    Components.showToast('Location removed.', 'success');
                    App.render();
                });
                break;

            // CPT Codes
            case 'add-cpt-code':
                Components.showModal('Add CPT Code', Views.renderCptCodeModal(), '');
                break;

            case 'confirm-add-cpt': {
                const code = document.getElementById('cptCode')?.value;
                const desc = document.getElementById('cptDescription')?.value;
                if (!code || !desc) {
                    Components.showToast('Please fill in all required fields.', 'error');
                    return;
                }
                AppState.addCptCode({ code, description: desc });
                Components.closeModal();
                Components.showToast('CPT code added.', 'success');
                App.render();
                break;
            }

            case 'remove-cpt':
                Components.confirmDanger('Remove CPT Code', `Remove CPT code ${el.dataset.code}?`, () => {
                    AppState.removeCptCode(el.dataset.code);
                    Components.closeModal();
                    Components.showToast('CPT code removed.', 'success');
                    App.render();
                });
                break;

            // Bulk Letters
            case 'new-bulk-letter':
                if (AppState.selectedPatientIds.length === 0) {
                    Components.showToast('Please select patients from the Patients page first.', 'error');
                    return;
                }
                Components.showModal('Send Bulk Letter', Views.renderBulkComposeModal(), '');
                break;

            // Visit Summary
            case 'view-visit-summary': {
                Components.showModal('Visit Summary', Views.renderVisitSummary(el.dataset.summary), '<button class="btn btn-secondary" data-action="close-modal">Close</button>');
                break;
            }

            // Modal
            case 'close-modal':
                Components.closeModal();
                break;

            case 'confirm-modal':
                if (window._modalConfirmCallback) {
                    window._modalConfirmCallback();
                    window._modalConfirmCallback = null;
                }
                break;

            default:
                console.warn('Unknown action:', action);
        }
    },

    // ── Dropdown Handler ────────────────────────────────────
    handleDropdownSelect(ddId, value) {
        // Update dropdown display text and selected class
        const dd = document.getElementById(ddId);
        if (dd) {
            const trigger = dd.querySelector('.dropdown-trigger');
            const item = dd.querySelector(`.dropdown-item[data-value="${value}"]`);
            if (trigger && item) {
                trigger.innerHTML = item.textContent + '<span class="dropdown-arrow">&#x25BC;</span>';
            }
            // Move 'selected' class to newly selected item
            dd.querySelectorAll('.dropdown-item.selected').forEach(el => el.classList.remove('selected'));
            if (item) item.classList.add('selected');
        }

        // Handle specific dropdowns
        switch (ddId) {
            case 'providerFilter':
                AppState.patientListFilter.providerId = value;
                AppState.patientListPage = 1;
                App.render();
                break;

            case 'routingProvider':
                AppState._routingSelectedProvider = value;
                App.render();
                break;
        }
    },

    // ── Toggle Handler ──────────────────────────────────────
    handleToggle(toggleId, checked) {
        switch (toggleId) {
            case 'allowPatientMessaging':
            case 'bookingSiteAutoInvite':
            case 'screenSharingPatients':
            case 'waitingRoomAudioNotification':
                // These are saved via save buttons
                break;
        }
    },

    // ── Checkbox Handler ────────────────────────────────────
    handleCheckbox(checkboxId, checked) {
        switch (checkboxId) {
            case 'filter-registered':
            case 'filter-invited':
            case 'filter-not_invited': {
                const status = checkboxId.replace('filter-', '');
                if (checked) {
                    if (!AppState.patientListFilter.passportStatus.includes(status)) {
                        AppState.patientListFilter.passportStatus.push(status);
                    }
                } else {
                    AppState.patientListFilter.passportStatus = AppState.patientListFilter.passportStatus.filter(s => s !== status);
                }
                AppState.patientListPage = 1;
                App.render();
                break;
            }
        }
    },

    // ── Helper to get dropdown value ────────────────────────
    _getDropdownValue(ddId) {
        const dd = document.getElementById(ddId);
        if (!dd) return null;
        const selected = dd.querySelector('.dropdown-item.selected');
        return selected ? selected.dataset.value : null;
    },

    // ── SSE ─────────────────────────────────────────────────
    setupSSE() {
        const evtSource = new EventSource('/api/events');
        evtSource.onmessage = (event) => {
            if (event.data === 'reset') {
                AppState.resetToSeedData();
                App.navigate('home');
            }
        };
        evtSource.onerror = () => {
            setTimeout(() => App.setupSSE(), 5000);
        };
    },

    // ── Initialization ──────────────────────────────────────
    initApp() {
        AppState.init();
        this.parseRoute();
        this.setupSSE();

        // Global click handler
        document.addEventListener('click', (e) => App.handleClick(e));

        // Hash change
        window.addEventListener('hashchange', () => {
            App.parseRoute();
            App.render();
        });

        // Menu toggle
        const menuToggle = document.getElementById('menuToggle');
        if (menuToggle) {
            menuToggle.addEventListener('click', () => {
                document.body.classList.toggle('sidebar-collapsed');
            });
        }

        // Subscribe to state changes
        AppState.subscribe(() => App.render());

        // Initial render
        App.render();

        // Push initial state to server
        AppState._pushStateToServer();
    }
};

document.addEventListener('DOMContentLoaded', () => {
    App.initApp();
});
