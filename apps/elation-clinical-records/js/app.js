/* ============================================================
   app.js — Routing, event handling, initialization
   ============================================================ */

const App = {
    _openDropdownId: null,
    _sseConnection: null,
    _dropdownValues: {},

    // ── Routing ──
    parseRoute() {
        const hash = window.location.hash.slice(2) || 'patients';
        const parts = hash.split('/');
        AppState.currentSection = parts[0] || 'patients';
        if (parts[0] === 'patients' && parts[1]) {
            AppState.selectedPatientId = parts[1];
            if (parts[2]) AppState.patientTab = parts[2];
        }
    },

    navigate(section) {
        window.location.hash = '#/' + section;
    },

    // ── Rendering ──
    render() {
        const sidebar = document.getElementById('sidebar');
        const content = document.getElementById('main-content');
        const modalContainer = document.getElementById('modal-container');
        const toastContainer = document.getElementById('toast-container');

        if (sidebar) sidebar.innerHTML = Views.renderSidebar();
        if (content) content.innerHTML = Views.renderContent();
        if (modalContainer) modalContainer.innerHTML = Views.renderModal();
        if (toastContainer) toastContainer.innerHTML = Views.renderToast();

        this._restoreDropdownStates();
    },

    _restoreDropdownStates() {
        if (this._openDropdownId) {
            const menu = document.querySelector(`[data-dropdown-menu="${this._openDropdownId}"]`);
            if (menu) menu.classList.add('open');
        }
    },

    // ── Event Handling ──
    handleClick(e) {
        const target = e.target;

        // Close dropdowns on outside click
        if (!target.closest('.custom-dropdown') && this._openDropdownId) {
            this._closeAllDropdowns();
        }

        // data-action routing
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            const action = actionEl.dataset.action;
            e.preventDefault();
            this._handleAction(action, actionEl);
            return;
        }

        // Dropdown trigger
        const trigger = target.closest('[data-dropdown-trigger]');
        if (trigger) {
            e.stopPropagation();
            this._toggleDropdown(trigger.dataset.dropdownTrigger);
            return;
        }

        // Dropdown item
        const item = target.closest('.dropdown-item');
        if (item) {
            const menu = item.closest('.dropdown-menu');
            const ddId = menu?.dataset.dropdownMenu;
            if (ddId) {
                this._selectDropdownValue(ddId, item.dataset.value);
            }
            return;
        }

        // Toggle switch
        const toggle = target.closest('.toggle-switch');
        if (toggle) {
            this._handleToggle(toggle.dataset.toggleId, toggle);
            return;
        }

        // Modal overlay click
        if (target.classList.contains('modal-overlay')) {
            AppState.activeModal = null;
            AppState.modalData = null;
            this.render();
        }
    },

    _handleAction(action, el) {
        switch (action) {
            // Navigation
            case 'navigate':
                AppState.selectedPatientId = null;
                AppState.patientTab = 'chart';
                this.navigate(el.dataset.section);
                break;
            case 'select-patient':
                AppState.selectedPatientId = el.dataset.patientId;
                AppState.patientTab = 'chart';
                this.navigate('patients/' + el.dataset.patientId);
                break;
            case 'back-to-list':
                AppState.selectedPatientId = null;
                this.navigate('patients');
                break;
            case 'switch-tab':
                AppState.patientTab = el.dataset.tab;
                this.render();
                break;

            // Problems
            case 'add-problem':
                AppState.activeModal = 'add-problem';
                AppState.modalData = null;
                this.render();
                break;
            case 'edit-problem': {
                const prob = AppState.problems.find(p => p.id === el.dataset.problemId);
                AppState.activeModal = 'edit-problem';
                AppState.modalData = prob ? { ...prob } : null;
                this.render();
                break;
            }
            case 'save-problem':
            case 'save-problem-and-add':
                this._saveProblem(action === 'save-problem-and-add');
                break;
            case 'save-edit-problem':
                this._saveEditProblem();
                break;
            case 'change-problem-status':
                AppState.changeProblemStatus(el.dataset.problemId, el.dataset.status);
                AppState.showToast(`Problem marked as ${el.dataset.status}`);
                break;
            case 'export-problem-to-note': {
                const prob2 = AppState.problems.find(p => p.id === el.dataset.problemId);
                if (prob2) {
                    AppState.showToast(`"${prob2.title}" exported to note assessment`);
                }
                break;
            }

            // Vaccinations
            case 'add-vaccination':
                AppState.activeModal = 'add-vaccination';
                AppState.modalData = {};
                this._dropdownValues = {};
                this.render();
                break;
            case 'save-vaccination':
            case 'save-vaccination-and-add':
                this._saveVaccination(action === 'save-vaccination-and-add');
                break;

            // Vitals
            case 'add-vitals':
                AppState.activeModal = 'add-vitals';
                AppState.modalData = null;
                this._dropdownValues = {};
                this.render();
                break;
            case 'save-vitals':
            case 'save-vitals-and-add':
                this._saveVitals(action === 'save-vitals-and-add');
                break;

            // Visit Notes
            case 'new-visit-note':
                AppState.activeModal = 'new-visit-note';
                AppState.modalData = null;
                this._dropdownValues = {};
                this.render();
                break;
            case 'create-visit-note':
                this._createVisitNote();
                break;
            case 'view-note': {
                const note = AppState.visitNotes.find(n => n.id === el.dataset.noteId);
                AppState.activeModal = 'view-note';
                AppState.modalData = note ? { ...note } : null;
                this.render();
                break;
            }
            case 'show-add-block':
                AppState.activeModal = 'add-block';
                AppState.modalData = { noteId: AppState.modalData?.id };
                this.render();
                break;
            case 'add-block-to-note': {
                const blockType = el.dataset.blockType;
                const noteId = el.dataset.noteId;
                AppState.addBlockToNote(noteId, { type: blockType, content: '' });
                const updatedNote = AppState.visitNotes.find(n => n.id === noteId);
                AppState.activeModal = 'view-note';
                AppState.modalData = updatedNote ? { ...updatedNote } : null;
                this.render();
                break;
            }
            case 'remove-block': {
                const blockIdx = parseInt(el.dataset.blockIdx);
                AppState.removeBlockFromNote(el.dataset.noteId, blockIdx);
                const updNote = AppState.visitNotes.find(n => n.id === el.dataset.noteId);
                AppState.modalData = updNote ? { ...updNote } : null;
                this.render();
                break;
            }
            case 'show-add-billing':
                AppState.activeModal = 'add-billing';
                AppState.modalData = { noteId: AppState.modalData?.id };
                this.render();
                break;
            case 'save-billing-item': {
                const cpt = document.getElementById('billing-cpt')?.value?.trim();
                const desc = document.getElementById('billing-description')?.value?.trim();
                if (!cpt || !desc) {
                    AppState.showToast('CPT code and description are required');
                    break;
                }
                const billingNoteId = AppState.modalData?.noteId;
                AppState.addBillingItemToNote(billingNoteId, { cptCode: cpt, description: desc });
                const updBillingNote = AppState.visitNotes.find(n => n.id === billingNoteId);
                AppState.activeModal = 'view-note';
                AppState.modalData = updBillingNote ? { ...updBillingNote } : null;
                this.render();
                break;
            }
            case 'remove-billing': {
                const billingIdx = parseInt(el.dataset.billingIdx);
                AppState.removeBillingItemFromNote(el.dataset.noteId, billingIdx);
                const updNote2 = AppState.visitNotes.find(n => n.id === el.dataset.noteId);
                AppState.modalData = updNote2 ? { ...updNote2 } : null;
                this.render();
                break;
            }
            case 'save-note-draft':
                this._saveNoteDraft();
                break;
            case 'sign-visit-note':
                this._signVisitNote();
                break;

            // Templates
            case 'new-template':
                AppState.activeModal = 'new-template';
                AppState.modalData = null;
                this.render();
                break;
            case 'edit-template': {
                const tmpl = AppState.visitNoteTemplates.find(t => t.id === el.dataset.templateId);
                AppState.activeModal = 'edit-template';
                AppState.modalData = tmpl ? { ...tmpl } : null;
                this.render();
                break;
            }
            case 'save-template':
                this._saveTemplate();
                break;
            case 'save-edit-template':
                this._saveEditTemplate();
                break;
            case 'duplicate-template':
                AppState.duplicateTemplate(el.dataset.templateId);
                AppState.showToast('Template duplicated');
                break;
            case 'delete-template':
                AppState.activeModal = 'confirm-delete';
                AppState.modalData = {
                    title: 'Delete Template',
                    message: 'Are you sure you want to delete this template?',
                    deleteAction: 'template',
                    deleteId: el.dataset.templateId
                };
                this.render();
                break;

            // Categories
            case 'add-category':
                AppState.activeModal = 'add-category';
                AppState.modalData = null;
                this._dropdownValues = {};
                this.render();
                break;
            case 'edit-category': {
                const cat = AppState.visitNoteCategories.find(c => c.id === el.dataset.categoryId);
                AppState.activeModal = 'edit-category';
                AppState.modalData = cat ? { ...cat } : null;
                this._dropdownValues = {};
                this.render();
                break;
            }
            case 'save-category':
                this._saveCategory();
                break;
            case 'save-edit-category':
                this._saveEditCategory();
                break;
            case 'remove-category':
                AppState.activeModal = 'confirm-delete';
                AppState.modalData = {
                    title: 'Remove Category',
                    message: 'Remove this category? Existing notes with this category will retain it, but no new notes can use it.',
                    deleteAction: 'category',
                    deleteId: el.dataset.categoryId
                };
                this.render();
                break;

            // Tags
            case 'add-tag':
                AppState.activeModal = 'add-tag';
                AppState.modalData = { patientId: el.dataset.patientId };
                this.render();
                break;
            case 'save-tag':
                this._saveTag();
                break;
            case 'remove-tag':
                AppState.removePatientTag(el.dataset.patientId, el.dataset.tag);
                AppState.showToast('Tag removed');
                break;

            // Appointment Types
            case 'edit-appointment-type': {
                const apt = AppState.appointmentTypes.find(a => a.id === el.dataset.aptId);
                AppState.activeModal = 'edit-appointment-type';
                AppState.modalData = apt ? { ...apt } : null;
                this._dropdownValues = {};
                this.render();
                break;
            }
            case 'save-appointment-type':
                this._saveAppointmentType();
                break;

            // Confirm delete
            case 'confirm-delete':
                this._executeDelete();
                break;

            // Care plan export
            case 'export-careplan':
                AppState.showToast('Care plan exported to new visit note');
                break;

            // Modal close
            case 'close-modal':
                AppState.activeModal = null;
                AppState.modalData = null;
                this._dropdownValues = {};
                this.render();
                break;
        }
    },

    // ── Dropdown Helpers ──
    _toggleDropdown(ddId) {
        if (this._openDropdownId === ddId) {
            this._closeAllDropdowns();
        } else {
            this._closeAllDropdowns();
            const menu = document.querySelector(`[data-dropdown-menu="${ddId}"]`);
            if (menu) {
                menu.classList.add('open');
                this._openDropdownId = ddId;
            }
        }
    },

    _closeAllDropdowns() {
        document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
        this._openDropdownId = null;
    },

    _selectDropdownValue(ddId, value) {
        this._dropdownValues[ddId] = value;
        const trigger = document.querySelector(`[data-dropdown-trigger="${ddId}"] .dropdown-value`);
        if (trigger) {
            // Find the label for this value
            const item = document.querySelector(`[data-dropdown-menu="${ddId}"] .dropdown-item[data-value="${CSS.escape(value)}"]`);
            trigger.textContent = item ? item.textContent : value;
        }

        // Update selected state visually
        const menu = document.querySelector(`[data-dropdown-menu="${ddId}"]`);
        if (menu) {
            menu.querySelectorAll('.dropdown-item').forEach(i => i.classList.remove('selected'));
            const sel = menu.querySelector(`.dropdown-item[data-value="${CSS.escape(value)}"]`);
            if (sel) sel.classList.add('selected');
        }

        this._closeAllDropdowns();

        // Handle preference dropdowns
        if (ddId === 'pref-note-format') {
            AppState.updatePreference('defaultNoteFormat', value);
        }
        // Problem status dropdown in modal
        if (ddId === 'problem-status') {
            // stored in _dropdownValues for form save
        }
    },

    // ── Toggle Helper ──
    _handleToggle(toggleId, el) {
        const isActive = el.classList.contains('active');
        el.classList.toggle('active');

        if (toggleId === 'pref-coded-assessments') {
            AppState.updatePreference('codedAssessments', !isActive);
        } else if (toggleId === 'pref-dx-in-print') {
            AppState.updatePreference('showDxCodesInPrint', !isActive);
        } else if (toggleId && toggleId.startsWith('mips-')) {
            const catId = toggleId.replace('mips-', '');
            AppState.updateCategory(catId, { countForMIPS: !isActive });
        } else if (toggleId === 'category-mips') {
            this._dropdownValues['category-mips'] = !isActive;
        }
    },

    // ── Input Handling ──
    handleInput(e) {
        const target = e.target;

        if (target.id === 'patient-search') {
            AppState.patientSearchQuery = target.value;
            this.render();
            const el = document.getElementById('patient-search');
            if (el) { el.focus(); el.selectionStart = el.selectionEnd = el.value.length; }
        }

        if (target.id === 'note-search') {
            AppState.noteSearchQuery = target.value;
            this.render();
            const el = document.getElementById('note-search');
            if (el) { el.focus(); el.selectionStart = el.selectionEnd = el.value.length; }
        }

        if (target.id === 'problem-search') {
            this._searchProblems(target.value);
        }

        if (target.id === 'vax-name') {
            this._searchVaccines(target.value);
        }
    },

    // ── Problem Search ──
    _searchProblems(query) {
        const results = document.getElementById('problem-search-results');
        if (!results) return;
        if (!query || query.length < 2) {
            results.innerHTML = '';
            return;
        }
        const q = query.toLowerCase();
        const matches = ICD10_DATABASE.filter(d =>
            d.code.toLowerCase().includes(q) || d.description.toLowerCase().includes(q)
        ).slice(0, 10);

        results.innerHTML = matches.map(d =>
            `<div class="search-result-item" data-icd="${d.code}" data-desc="${Components.escAttr(d.description)}">
                <span class="icd-code">${Components.esc(d.code)}</span> ${Components.esc(d.description)}
            </div>`
        ).join('');

        results.querySelectorAll('.search-result-item').forEach(item => {
            item.addEventListener('click', () => {
                const titleInput = document.getElementById('problem-title');
                const icdInput = document.getElementById('problem-icd10');
                if (titleInput) titleInput.value = item.dataset.desc;
                if (icdInput) icdInput.value = item.dataset.icd;
                results.innerHTML = '';
            });
        });
    },

    // ── Vaccine Search ──
    _searchVaccines(query) {
        const results = document.getElementById('vax-name-results');
        if (!results) return;
        if (!query || query.length < 2) {
            results.innerHTML = '';
            return;
        }
        const q = query.toLowerCase();
        const matches = VACCINE_NAME_OPTIONS.filter(v => v.toLowerCase().includes(q)).slice(0, 8);
        results.innerHTML = matches.map(v =>
            `<div class="search-result-item" data-vax-name="${Components.escAttr(v)}">${Components.esc(v)}</div>`
        ).join('');

        results.querySelectorAll('.search-result-item').forEach(item => {
            item.addEventListener('click', () => {
                const nameInput = document.getElementById('vax-name');
                if (nameInput) nameInput.value = item.dataset.vaxName;
                results.innerHTML = '';
            });
        });
    },

    // ── Form Save Handlers ──
    _saveProblem(addAnother) {
        const title = document.getElementById('problem-title')?.value?.trim();
        if (!title) {
            AppState.showToast('Problem title is required');
            return;
        }
        const data = {
            title,
            icd10: document.getElementById('problem-icd10')?.value?.trim() || '',
            dxDate: document.getElementById('problem-dx-date')?.value?.trim() || '',
            status: this._dropdownValues['problem-status'] || 'Active',
            synopsis: document.getElementById('problem-synopsis')?.value?.trim() || ''
        };
        AppState.addProblem(AppState.selectedPatientId, data);
        AppState.showToast('Problem added');
        if (addAnother) {
            AppState.activeModal = 'add-problem';
            AppState.modalData = null;
            this._dropdownValues = {};
            this.render();
        } else {
            AppState.activeModal = null;
            this.render();
        }
    },

    _saveEditProblem() {
        const prob = AppState.modalData;
        if (!prob) return;
        const title = document.getElementById('problem-title')?.value?.trim();
        if (!title) {
            AppState.showToast('Problem title is required');
            return;
        }
        AppState.updateProblem(prob.id, {
            title,
            icd10: document.getElementById('problem-icd10')?.value?.trim() || '',
            dxDate: document.getElementById('problem-dx-date')?.value?.trim() || '',
            status: this._dropdownValues['problem-status'] || prob.status,
            synopsis: document.getElementById('problem-synopsis')?.value?.trim() || ''
        });
        AppState.activeModal = null;
        AppState.modalData = null;
        AppState.showToast('Problem updated');
        this.render();
    },

    _saveVaccination(addAnother) {
        const name = document.getElementById('vax-name')?.value?.trim();
        if (!name) {
            AppState.showToast('Vaccine name is required');
            return;
        }
        const data = {
            vaccineName: name,
            recordType: this._dropdownValues['vax-record-type'] || 'New',
            manufacturer: this._dropdownValues['vax-manufacturer'] || '',
            lotNumber: document.getElementById('vax-lot')?.value?.trim() || '',
            ndc: document.getElementById('vax-ndc')?.value?.trim() || '',
            expirationDate: document.getElementById('vax-expiration')?.value?.trim() || '',
            doseAmount: document.getElementById('vax-dose-amount')?.value?.trim() || '',
            doseUnits: this._dropdownValues['vax-dose-units'] || 'mL',
            seriesNumber: document.getElementById('vax-series')?.value?.trim() || '',
            method: this._dropdownValues['vax-method'] || '',
            site: this._dropdownValues['vax-site'] || '',
            givenOn: document.getElementById('vax-given-on')?.value?.trim() || new Date().toISOString(),
            visDate: document.getElementById('vax-vis-date')?.value?.trim() || '',
            orderedBy: this._dropdownValues['vax-ordered-by'] || AppState.currentProvider.id,
            givenBy: document.getElementById('vax-given-by')?.value?.trim() || '',
            recall: this._dropdownValues['vax-recall'] || '',
            program: this._dropdownValues['vax-program'] || 'Not VFC Eligible',
            fundedBy: this._dropdownValues['vax-funded-by'] || 'Private',
            reason: document.getElementById('vax-reason')?.value?.trim() || '',
            notes: document.getElementById('vax-notes')?.value?.trim() || '',
            isInjectable: !!document.querySelector('[data-toggle-id="vax-is-injectable"]')?.classList.contains('active'),
            notSendToRegistry: !!document.querySelector('[data-toggle-id="vax-not-send-registry"]')?.classList.contains('active')
        };
        AppState.addVaccination(AppState.selectedPatientId, data);
        AppState.showToast('Vaccination recorded');
        if (addAnother) {
            AppState.activeModal = 'add-vaccination';
            AppState.modalData = {};
            this._dropdownValues = {};
            this.render();
        } else {
            AppState.activeModal = null;
            this._dropdownValues = {};
            this.render();
        }
    },

    _saveVitals(addAnother) {
        const dateVal = document.getElementById('vitals-date')?.value?.trim();
        const sys = document.getElementById('vitals-sys')?.value?.trim();
        const dia = document.getElementById('vitals-dia')?.value?.trim();
        if (!sys && !dia && !document.getElementById('vitals-hr')?.value?.trim() && !document.getElementById('vitals-temp')?.value?.trim() && !document.getElementById('vitals-weight')?.value?.trim()) {
            AppState.showToast('Please enter at least one vital sign');
            return;
        }

        const w = parseFloat(document.getElementById('vitals-weight')?.value) || null;
        const h = parseFloat(document.getElementById('vitals-height')?.value) || null;
        const wUnit = this._dropdownValues['vitals-weight-unit'] || 'lbs';
        const hUnit = this._dropdownValues['vitals-height-unit'] || 'in';
        let bmi = null;
        if (w && h) {
            let wKg = wUnit === 'kg' ? w : w * 0.453592;
            let hM = hUnit === 'cm' ? h / 100 : h * 0.0254;
            if (hM > 0) bmi = Math.round((wKg / (hM * hM)) * 10) / 10;
        }

        const data = {
            date: dateVal ? new Date(dateVal).toISOString() : new Date().toISOString(),
            bloodPressureSystolic: parseInt(sys) || null,
            bloodPressureDiastolic: parseInt(dia) || null,
            heartRate: parseInt(document.getElementById('vitals-hr')?.value) || null,
            respiratoryRate: parseInt(document.getElementById('vitals-rr')?.value) || null,
            temperature: parseFloat(document.getElementById('vitals-temp')?.value) || null,
            temperatureUnit: this._dropdownValues['vitals-temp-unit'] || 'F',
            oxygenSaturation: parseInt(document.getElementById('vitals-spo2')?.value) || null,
            weight: w, weightUnit: wUnit,
            height: h, heightUnit: hUnit,
            bmi,
            painLevel: document.getElementById('vitals-pain')?.value?.trim() !== '' ? parseInt(document.getElementById('vitals-pain')?.value) : null
        };
        AppState.addVitals(AppState.selectedPatientId, 'note_hist_' + Date.now(), data);
        AppState.showToast('Vitals recorded');
        if (addAnother) {
            AppState.activeModal = 'add-vitals';
            this._dropdownValues = {};
            this.render();
        } else {
            AppState.activeModal = null;
            this._dropdownValues = {};
            this.render();
        }
    },

    _createVisitNote() {
        const reason = document.getElementById('note-reason')?.value?.trim() || '';
        const format = this._dropdownValues['note-format'] || AppState.providerPreferences.defaultNoteFormat;
        const category = this._dropdownValues['note-category'] || AppState.visitNoteCategories.find(c => c.isDefault)?.id || 'cat_001';
        const templateId = this._dropdownValues['note-template'] || '';
        const date = document.getElementById('note-date')?.value?.trim() || new Date().toISOString().split('T')[0];

        let blocks = [];
        let billingItems = [];
        let documentTags = [];

        if (templateId) {
            const tmpl = AppState.visitNoteTemplates.find(t => t.id === templateId);
            if (tmpl) {
                Object.entries(tmpl.content).forEach(([type, content]) => {
                    blocks.push({ type, content });
                });
                billingItems = [...(tmpl.billingItems || [])];
                documentTags = [...(tmpl.documentTags || [])];
            }
        }

        const note = AppState.addVisitNote(AppState.selectedPatientId, {
            format, category, templateUsed: templateId,
            date: new Date(date).toISOString(),
            reason, blocks, billingItems, documentTags
        });
        AppState.activeModal = 'view-note';
        AppState.modalData = { ...note };
        this._dropdownValues = {};
        AppState.showToast('Visit note created');
        this.render();
    },

    _saveNoteDraft() {
        const note = AppState.modalData;
        if (!note) return;
        // Save block content from textareas
        const textareas = document.querySelectorAll('.block-content[data-block-idx]');
        textareas.forEach(ta => {
            const idx = parseInt(ta.dataset.blockIdx);
            AppState.updateNoteBlock(note.id, idx, ta.value);
        });
        const updNote = AppState.visitNotes.find(n => n.id === note.id);
        AppState.modalData = updNote ? { ...updNote } : null;
        AppState.showToast('Draft saved');
        this.render();
    },

    _signVisitNote() {
        const note = AppState.modalData;
        if (!note) return;
        // Save content first
        const textareas = document.querySelectorAll('.block-content[data-block-idx]');
        textareas.forEach(ta => {
            const idx = parseInt(ta.dataset.blockIdx);
            AppState.updateNoteBlock(note.id, idx, ta.value);
        });
        AppState.signVisitNote(note.id);
        const updNote = AppState.visitNotes.find(n => n.id === note.id);
        AppState.modalData = updNote ? { ...updNote } : null;
        AppState.showToast('Visit note signed');
        this.render();
    },

    _saveTemplate() {
        const name = document.getElementById('template-name')?.value?.trim();
        if (!name) {
            AppState.showToast('Template name is required');
            return;
        }
        const content = {};
        const hpi = document.getElementById('template-hpi')?.value?.trim();
        const ros = document.getElementById('template-ros')?.value?.trim();
        const pe = document.getElementById('template-pe')?.value?.trim();
        const assessment = document.getElementById('template-assessment')?.value?.trim();
        if (hpi) content.hpi = hpi;
        if (ros) content.ros = ros;
        if (pe) content.pe = pe;
        if (assessment) content.assessment = assessment;

        const billingItems = [];
        const cpt = document.getElementById('template-cpt')?.value?.trim();
        const cptDesc = document.getElementById('template-cpt-desc')?.value?.trim();
        if (cpt) billingItems.push({ cptCode: cpt, description: cptDesc || '' });

        const pos = document.getElementById('template-pos')?.value?.trim() || '';
        const billingNotes = document.getElementById('template-billing-notes')?.value?.trim() || '';
        const tagsStr = document.getElementById('template-tags')?.value?.trim() || '';
        const documentTags = tagsStr ? tagsStr.split(',').map(t => t.trim()).filter(t => t) : [];

        AppState.addTemplate({ name, content, billingItems, pos, billingNotes, documentTags });
        AppState.activeModal = null;
        AppState.showToast('Template created');
        this.render();
    },

    _saveEditTemplate() {
        const tmpl = AppState.modalData;
        if (!tmpl) return;
        const name = document.getElementById('template-name')?.value?.trim();
        if (!name) {
            AppState.showToast('Template name is required');
            return;
        }
        const content = {};
        const hpi = document.getElementById('template-hpi')?.value?.trim();
        const ros = document.getElementById('template-ros')?.value?.trim();
        const pe = document.getElementById('template-pe')?.value?.trim();
        const assessment = document.getElementById('template-assessment')?.value?.trim();
        if (hpi) content.hpi = hpi;
        if (ros) content.ros = ros;
        if (pe) content.pe = pe;
        if (assessment) content.assessment = assessment;

        const billingItems = [];
        const cpt = document.getElementById('template-cpt')?.value?.trim();
        const cptDesc = document.getElementById('template-cpt-desc')?.value?.trim();
        if (cpt) billingItems.push({ cptCode: cpt, description: cptDesc || '' });

        const pos = document.getElementById('template-pos')?.value?.trim() || '';
        const billingNotes = document.getElementById('template-billing-notes')?.value?.trim() || '';
        const tagsStr = document.getElementById('template-tags')?.value?.trim() || '';
        const documentTags = tagsStr ? tagsStr.split(',').map(t => t.trim()).filter(t => t) : [];

        AppState.updateTemplate(tmpl.id, { name, content, billingItems, pos, billingNotes, documentTags });
        AppState.activeModal = null;
        AppState.showToast('Template updated');
        this.render();
    },

    _saveCategory() {
        const name = document.getElementById('category-name')?.value?.trim();
        if (!name) {
            AppState.showToast('Category name is required');
            return;
        }
        const mips = this._dropdownValues['category-mips'] || false;
        AppState.addCategory({ name, countForMIPS: mips });
        AppState.activeModal = null;
        AppState.showToast('Category added');
        this.render();
    },

    _saveEditCategory() {
        const cat = AppState.modalData;
        if (!cat) return;
        const name = document.getElementById('category-name')?.value?.trim();
        if (!name) {
            AppState.showToast('Category name is required');
            return;
        }
        const mipsToggle = document.querySelector('[data-toggle-id="category-mips"]');
        const mips = mipsToggle ? mipsToggle.classList.contains('active') : cat.countForMIPS;
        AppState.updateCategory(cat.id, { name, countForMIPS: mips });
        AppState.activeModal = null;
        AppState.showToast('Category updated');
        this.render();
    },

    _saveTag() {
        const tag = document.getElementById('tag-name')?.value?.trim();
        if (!tag) {
            AppState.showToast('Tag name is required');
            return;
        }
        const patientId = AppState.modalData?.patientId;
        if (patientId) {
            AppState.addPatientTag(patientId, tag);
            AppState.showToast('Tag added');
        }
        AppState.activeModal = null;
        this.render();
    },

    _saveAppointmentType() {
        const apt = AppState.modalData;
        if (!apt) return;
        const updates = {
            noteFormat: this._dropdownValues['apt-note-format'] || apt.noteFormat,
            noteCategory: this._dropdownValues['apt-note-category'] || apt.noteCategory,
            noteTemplate: this._dropdownValues['apt-note-template'] !== undefined ? this._dropdownValues['apt-note-template'] : apt.noteTemplate
        };
        AppState.updateAppointmentType(apt.id, updates);
        AppState.activeModal = null;
        this._dropdownValues = {};
        AppState.showToast('Appointment type updated');
        this.render();
    },

    _executeDelete() {
        const data = AppState.modalData;
        if (!data) return;
        if (data.deleteAction === 'template') {
            AppState.deleteTemplate(data.deleteId);
            AppState.showToast('Template deleted');
        } else if (data.deleteAction === 'category') {
            AppState.removeCategory(data.deleteId);
            AppState.showToast('Category removed');
        }
        AppState.activeModal = null;
        AppState.modalData = null;
        this.render();
    },

    // ── Keyboard Handling ──
    handleKeydown(e) {
        if (e.key === 'Escape') {
            if (this._openDropdownId) {
                this._closeAllDropdowns();
            } else if (AppState.activeModal) {
                AppState.activeModal = null;
                AppState.modalData = null;
                this.render();
            }
        }
    },

    // ── SSE ──
    _initSSE() {
        const eventSource = new EventSource('/api/events');
        eventSource.onmessage = (e) => {
            if (e.data === 'reset') {
                AppState.resetToSeedData();
                window.location.hash = '#/patients';
            }
        };
        this._sseConnection = eventSource;
    },

    // ── Init ──
    init() {
        AppState.init();
        AppState.subscribe(() => this.render());
        this.parseRoute();
        this.render();
        AppState._pushStateToServer();

        document.addEventListener('click', (e) => this.handleClick(e));
        document.addEventListener('keydown', (e) => this.handleKeydown(e));
        document.addEventListener('input', (e) => this.handleInput(e));
        window.addEventListener('hashchange', () => {
            this.parseRoute();
            this.render();
        });

        this._initSSE();
    }
};

document.addEventListener('DOMContentLoaded', () => App.init());
