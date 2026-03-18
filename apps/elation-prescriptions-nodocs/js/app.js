/* Elation Prescriptions — App Router & Event Delegation */
const App = (function() {
    let _searchTimeout = null;

    function init() {
        AppState.init();
        _setupSSE();
        AppState.subscribe(_render);
        _render();
        document.addEventListener('click', _handleClick);
        document.addEventListener('input', _handleInput);
        document.addEventListener('change', _handleChange);
        document.addEventListener('keydown', _handleKeydown);
    }

    function _setupSSE() {
        const es = new EventSource('/api/events');
        es.onmessage = function(e) {
            if (e.data === 'reset') {
                AppState.resetToSeedData();
            }
        };
    }

    function _render() {
        const sidebar = document.getElementById('sidebar-nav');
        if (sidebar) sidebar.innerHTML = Views.renderSidebar();

        const content = document.getElementById('main-content');
        if (content) content.innerHTML = Views.renderContent();

        const patientSel = document.getElementById('patient-selector-container');
        if (patientSel) patientSel.innerHTML = Views.renderPatientSelector();
    }

    // ==================== CLICK HANDLER ====================
    function _handleClick(e) {
        const target = e.target;

        // Close all dropdowns when clicking outside
        if (!target.closest('.custom-dropdown') && !target.closest('.searchable-dropdown') && !target.closest('.patient-selector')) {
            _closeAllDropdowns();
        }

        // Modal overlay click
        if (target.id === 'modal-overlay' || target.closest('[data-action="close-modal"]')) {
            Components.closeModal();
            return;
        }

        // Modal confirm
        if (target.closest('[data-action="confirm-modal"]')) {
            const cb = Components.getConfirmCallback();
            Components.closeModal();
            if (cb) cb();
            return;
        }

        // Route navigation
        const routeEl = target.closest('[data-route]');
        if (routeEl) {
            const route = routeEl.dataset.route;
            AppState.set('currentView', route);
            AppState.set('currentPrescriptionId', null);
            AppState.set('currentPage', 1);
            AppState.notify();
            return;
        }

        // Dropdown trigger
        const dropdownTrigger = target.closest('[data-dropdown-trigger]');
        if (dropdownTrigger) {
            const dropdownId = dropdownTrigger.dataset.dropdownTrigger;
            _toggleDropdown(dropdownId);
            return;
        }

        // Dropdown item
        const dropdownItem = target.closest('[data-dropdown-item]');
        if (dropdownItem) {
            const dropdownId = dropdownItem.dataset.dropdownItem;
            const value = dropdownItem.dataset.value;
            _handleDropdownSelect(dropdownId, value);
            return;
        }

        // Toggle switch
        const toggleEl = target.closest('[data-toggle]');
        if (toggleEl) {
            toggleEl.classList.toggle('active');
            _handleToggle(toggleEl.dataset.toggle, toggleEl.classList.contains('active'));
            return;
        }

        // Action buttons
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            _handleAction(actionEl);
            return;
        }
    }

    // ==================== INPUT HANDLER ====================
    function _handleInput(e) {
        const target = e.target;

        // Drug search in prescribe form
        if (target.id === 'drug-search-input') {
            clearTimeout(_searchTimeout);
            _searchTimeout = setTimeout(() => _handleDrugSearch(target.value), 200);
            return;
        }

        // Interaction checker drug search
        if (target.id === 'interaction-drug-input') {
            clearTimeout(_searchTimeout);
            _searchTimeout = setTimeout(() => _handleInteractionDrugSearch(target.value), 200);
            return;
        }

        // Medication list search
        if (target.id === 'med-search') {
            clearTimeout(_searchTimeout);
            _searchTimeout = setTimeout(() => {
                AppState.set('searchQuery', target.value);
                AppState.set('currentPage', 1);
                AppState.notify();
            }, 300);
            return;
        }

        // History filter inputs
        if (target.id === 'history-date-from' || target.id === 'history-date-to' || target.id === 'history-medication') {
            clearTimeout(_searchTimeout);
            _searchTimeout = setTimeout(() => {
                const f = AppState.get('historyFilter');
                f.dateFrom = document.getElementById('history-date-from')?.value || '';
                f.dateTo = document.getElementById('history-date-to')?.value || '';
                f.medication = document.getElementById('history-medication')?.value || '';
                AppState.set('historyFilter', f);
                AppState.notify();
            }, 300);
            return;
        }
    }

    function _handleChange(e) {
        // No special change handlers needed beyond input
    }

    function _handleKeydown(e) {
        if (e.key === 'Escape') {
            _closeAllDropdowns();
            Components.closeModal();
        }
    }

    // ==================== DROPDOWN LOGIC ====================
    function _toggleDropdown(id) {
        const menu = document.getElementById(id + '-menu');
        if (!menu) return;
        const wasOpen = menu.classList.contains('open');
        _closeAllDropdowns();
        if (!wasOpen) {
            menu.classList.add('open');
        }
    }

    function _closeAllDropdowns() {
        document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
    }

    function _handleDropdownSelect(dropdownId, value) {
        _closeAllDropdowns();

        switch (dropdownId) {
            case 'patient-selector':
                AppState.switchPatient(value);
                break;
            case 'med-sort-dropdown':
                AppState.set('medicationSort', value);
                AppState.notify();
                break;
            case 'form-strength-dropdown':
                _updatePrescribeFormData('formStrength', value);
                // Auto-fill dosage from strength
                const dosage = value.split(' ')[0];
                _updatePrescribeFormData('dosage', dosage);
                break;
            case 'frequency-dropdown':
                _updatePrescribeFormData('frequency', value);
                break;
            case 'route-dropdown':
                _updatePrescribeFormData('route', value);
                break;
            case 'pharmacy-dropdown':
                _updatePrescribeFormData('pharmacyId', value);
                break;
            case 'history-provider-dropdown':
                const hf = AppState.get('historyFilter');
                hf.provider = value;
                AppState.set('historyFilter', hf);
                AppState.notify();
                break;
            case 'default-pharmacy-dropdown':
                // Settings change — will be saved on "Save Settings"
                AppState.get('settings').defaultPharmacy = value;
                _render();
                break;
            case 'print-format-dropdown':
                AppState.get('settings').printFormat = value;
                _render();
                break;
        }
    }

    // ==================== ACTION HANDLER ====================
    function _handleAction(el) {
        const action = el.dataset.action;
        switch (action) {
            case 'new-prescription':
                AppState.set('currentView', 'prescribe');
                AppState.set('prescribeFormData', null);
                AppState.notify();
                break;
            case 'view-prescription':
                AppState.set('currentView', 'prescription-detail');
                AppState.set('currentPrescriptionId', el.dataset.rxId || el.closest('[data-rx-id]')?.dataset.rxId);
                AppState.notify();
                break;
            case 'back-to-medications':
                AppState.set('currentView', 'medications');
                AppState.set('currentPrescriptionId', null);
                AppState.notify();
                break;
            case 'set-med-filter':
                AppState.set('medicationFilter', el.dataset.value);
                AppState.set('currentPage', 1);
                AppState.notify();
                break;
            case 'set-refill-filter':
                AppState.set('refillFilter', el.dataset.value);
                AppState.notify();
                break;
            case 'search-medications':
                // Handled by input handler
                break;
            case 'select-sig':
                const sigInput = document.getElementById('sig-input');
                if (sigInput) {
                    sigInput.value = el.dataset.sig;
                    _updatePrescribeFormData('sig', el.dataset.sig);
                }
                break;
            case 'select-favorite-drug':
                _selectDrugForPrescribe(el.dataset.drugId);
                break;
            case 'cancel-prescribe':
                AppState.set('currentView', 'medications');
                AppState.set('prescribeFormData', null);
                AppState.notify();
                break;
            case 'submit-prescription':
                _submitPrescription();
                break;
            case 'print-prescription':
                Components.showToast('Prescription sent to printer', 'success');
                break;
            case 'renew-prescription':
                _showRenewModal(el.dataset.rxId);
                break;
            case 'modify-prescription':
                _showModifyModal(el.dataset.rxId);
                break;
            case 'discontinue-prescription':
                _showDiscontinueModal(el.dataset.rxId);
                break;
            case 'hold-prescription':
                _showHoldModal(el.dataset.rxId);
                break;
            case 'resume-prescription':
                Components.confirm('Resume Prescription', 'Resume this prescription from hold?', () => {
                    AppState.resumePrescription(el.dataset.rxId);
                    Components.showToast('Prescription resumed', 'success');
                });
                break;
            case 'represcribe':
                _represcribe(el.dataset.rxId);
                break;
            case 'toggle-favorite-drug':
                AppState.toggleFavoriteDrug(el.dataset.drugId);
                break;
            case 'approve-refill':
                Components.confirm('Approve Refill', 'Approve this refill request?', () => {
                    AppState.approveRefillRequest(el.dataset.rrId);
                    Components.showToast('Refill approved', 'success');
                });
                break;
            case 'deny-refill':
                _showDenyRefillModal(el.dataset.rrId);
                break;
            case 'modify-refill':
                _showModifyRefillModal(el.dataset.rrId);
                break;
            case 'load-patient-meds':
                _loadPatientMedsForInteractionCheck();
                break;
            case 'remove-interaction-drug':
                _removeInteractionDrug(el.dataset.drugId);
                break;
            case 'clear-interaction-drugs':
                AppState.set('interactionCheckDrugs', []);
                _render();
                break;
            case 'save-settings':
                _saveSettings();
                break;
            case 'remove-favorite':
                AppState.toggleFavoriteDrug(el.dataset.drugId);
                break;
            case 'goto-page':
                AppState.set('currentPage', parseInt(el.dataset.page));
                AppState.notify();
                break;
            case 'prev-page':
                AppState.set('currentPage', Math.max(1, AppState.get('currentPage') - 1));
                AppState.notify();
                break;
            case 'next-page':
                AppState.set('currentPage', AppState.get('currentPage') + 1);
                AppState.notify();
                break;
        }
    }

    // ==================== DRUG SEARCH ====================
    function _handleDrugSearch(query) {
        const results = AppState.searchDrugs(query);
        const container = document.getElementById('drug-search-results');
        if (!container) return;
        if (results.length === 0 && query.length >= 2) {
            container.innerHTML = '<div class="dropdown-item disabled">No drugs found</div>';
            container.classList.add('open');
            return;
        }
        if (results.length === 0) {
            container.classList.remove('open');
            return;
        }
        const settings = AppState.get('settings');
        container.innerHTML = results.slice(0, 15).map(d => {
            const isFav = AppState.isFavoriteDrug(d.id);
            const displayName = settings.showGenericFirst
                ? `${d.genericName} (${d.brandName})`
                : `${d.brandName} (${d.genericName})`;
            return `<div class="dropdown-item drug-result" data-action="select-drug-result" data-drug-id="${d.id}">
                <div class="drug-result-name">${isFav ? '&#9733; ' : ''}${Components.escapeHtml(displayName)}</div>
                <div class="drug-result-class">${Components.escapeHtml(d.drugClass)}${d.schedule ? ' | Schedule ' + d.schedule : ''}</div>
            </div>`;
        }).join('');
        container.classList.add('open');

        // Attach click handlers to results
        container.querySelectorAll('[data-action="select-drug-result"]').forEach(el => {
            el.addEventListener('click', (e) => {
                e.stopPropagation();
                _selectDrugForPrescribe(el.dataset.drugId);
                container.classList.remove('open');
            });
        });
    }

    function _selectDrugForPrescribe(drugId) {
        const drug = AppState.getDrugById(drugId);
        if (!drug) return;
        const patient = AppState.getCurrentPatient();
        const formData = {
            drugId: drug.id,
            drugName: drug.genericName,
            brandName: drug.brandName,
            formStrength: null,
            dosage: '',
            frequency: drug.commonSigs[0] ? '' : '',
            route: drug.routes[0] || '',
            quantity: '',
            daysSupply: AppState.get('settings').defaultDaysSupply,
            refills: AppState.get('settings').defaultRefills,
            sig: '',
            daw: false,
            pharmacyId: patient ? patient.preferredPharmacy : AppState.get('settings').defaultPharmacy,
            priorAuth: false,
            priorAuthNumber: '',
            note: ''
        };
        AppState.set('prescribeFormData', formData);
        AppState.set('currentView', 'prescribe');
        AppState.notify();
    }

    function _updatePrescribeFormData(field, value) {
        let formData = AppState.get('prescribeFormData');
        if (!formData) {
            formData = {};
            AppState.set('prescribeFormData', formData);
        }
        formData[field] = value;
        // Re-render to show updated form
        _render();
    }

    // ==================== SUBMIT PRESCRIPTION ====================
    function _submitPrescription() {
        const formData = AppState.get('prescribeFormData');
        if (!formData || !formData.drugId) {
            Components.showToast('Please select a medication', 'error');
            return;
        }
        if (!formData.formStrength) {
            Components.showToast('Please select a form and strength', 'error');
            return;
        }
        if (!formData.frequency) {
            Components.showToast('Please select a frequency', 'error');
            return;
        }
        if (!formData.route) {
            Components.showToast('Please select a route', 'error');
            return;
        }

        // Gather remaining form values
        const sigInput = document.getElementById('sig-input');
        if (sigInput) formData.sig = sigInput.value;
        const qtyInput = document.getElementById('quantity-input');
        if (qtyInput) formData.quantity = qtyInput.value;
        const dsInput = document.getElementById('days-supply-input');
        if (dsInput) formData.daysSupply = dsInput.value;
        const refInput = document.getElementById('refills-input');
        if (refInput) formData.refills = refInput.value;
        const dosageInput = document.getElementById('dosage-input');
        if (dosageInput) formData.dosage = dosageInput.value;
        const noteInput = document.getElementById('prescribe-note');
        if (noteInput) formData.note = noteInput.value;
        const paInput = document.getElementById('prior-auth-number');
        if (paInput) formData.priorAuthNumber = paInput.value;

        if (!formData.sig) {
            Components.showToast('Please enter directions (sig)', 'error');
            return;
        }
        if (!formData.pharmacyId) {
            Components.showToast('Please select a pharmacy', 'error');
            return;
        }

        const rx = AppState.createPrescription(formData);
        AppState.set('prescribeFormData', null);
        AppState.set('currentView', 'prescription-detail');
        AppState.set('currentPrescriptionId', rx.id);
        AppState.notify();
        Components.showToast('Prescription created successfully', 'success');
    }

    // ==================== PRESCRIPTION ACTIONS ====================
    function _showRenewModal(rxId) {
        const rx = AppState.getPrescriptionById(rxId);
        if (!rx) return;
        const body = `
            <p>Renew prescription for <strong>${Components.escapeHtml(rx.drugName)} ${Components.escapeHtml(rx.formStrength)}</strong></p>
            <div class="form-group">
                <label for="renew-refills">Number of Refills</label>
                <input type="text" inputmode="numeric" id="renew-refills" class="form-input" value="${rx.refillsTotal}" placeholder="Number of refills">
            </div>`;
        const footer = `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                        <button class="btn btn-primary" id="confirm-renew-btn">Renew</button>`;
        Components.showModal('Renew Prescription', body, footer);
        setTimeout(() => {
            document.getElementById('confirm-renew-btn')?.addEventListener('click', () => {
                const refills = document.getElementById('renew-refills')?.value || rx.refillsTotal;
                AppState.renewPrescription(rxId, refills);
                Components.closeModal();
                Components.showToast('Prescription renewed', 'success');
            });
        }, 50);
    }

    function _showModifyModal(rxId) {
        const rx = AppState.getPrescriptionById(rxId);
        if (!rx) return;
        const body = `
            <p>Modify prescription for <strong>${Components.escapeHtml(rx.drugName)}</strong></p>
            <div class="form-group">
                <label for="modify-dosage">Dosage</label>
                <input type="text" id="modify-dosage" class="form-input" value="${Components.escapeAttr(rx.dosage)}">
            </div>
            <div class="form-group">
                <label for="modify-frequency">Frequency</label>
                <input type="text" id="modify-frequency" class="form-input" value="${Components.escapeAttr(rx.frequency)}">
            </div>
            <div class="form-group">
                <label for="modify-sig">Directions</label>
                <textarea id="modify-sig" class="form-input form-textarea" rows="2">${Components.escapeHtml(rx.sig)}</textarea>
            </div>
            <div class="form-group">
                <label for="modify-quantity">Quantity</label>
                <input type="text" inputmode="numeric" id="modify-quantity" class="form-input" value="${rx.quantity}">
            </div>`;
        const footer = `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                        <button class="btn btn-primary" id="confirm-modify-btn">Save Changes</button>`;
        Components.showModal('Modify Prescription', body, footer);
        setTimeout(() => {
            document.getElementById('confirm-modify-btn')?.addEventListener('click', () => {
                const changes = {};
                const dosageVal = document.getElementById('modify-dosage')?.value;
                const freqVal = document.getElementById('modify-frequency')?.value;
                const sigVal = document.getElementById('modify-sig')?.value;
                const qtyVal = document.getElementById('modify-quantity')?.value;
                if (dosageVal !== rx.dosage) changes.dosage = dosageVal;
                if (freqVal !== rx.frequency) changes.frequency = freqVal;
                if (sigVal !== rx.sig) changes.sig = sigVal;
                if (parseInt(qtyVal) !== rx.quantity) changes.quantity = parseInt(qtyVal);
                AppState.modifyPrescription(rxId, changes);
                Components.closeModal();
                Components.showToast('Prescription modified', 'success');
            });
        }, 50);
    }

    function _showDiscontinueModal(rxId) {
        const rx = AppState.getPrescriptionById(rxId);
        if (!rx) return;
        const body = `
            <p>Discontinue <strong>${Components.escapeHtml(rx.drugName)} ${Components.escapeHtml(rx.formStrength)}</strong></p>
            <div class="form-group">
                <label for="dc-reason">Reason for Discontinuation <span class="required">*</span></label>
                <textarea id="dc-reason" class="form-input form-textarea" rows="2" placeholder="Enter reason..."></textarea>
            </div>`;
        const footer = `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                        <button class="btn btn-danger" id="confirm-dc-btn">Discontinue</button>`;
        Components.showModal('Discontinue Prescription', body, footer);
        setTimeout(() => {
            document.getElementById('confirm-dc-btn')?.addEventListener('click', () => {
                const reason = document.getElementById('dc-reason')?.value;
                if (!reason) {
                    Components.showToast('Please enter a reason', 'error');
                    return;
                }
                AppState.discontinuePrescription(rxId, reason);
                Components.closeModal();
                Components.showToast('Prescription discontinued', 'success');
            });
        }, 50);
    }

    function _showHoldModal(rxId) {
        const rx = AppState.getPrescriptionById(rxId);
        if (!rx) return;
        const body = `
            <p>Place <strong>${Components.escapeHtml(rx.drugName)} ${Components.escapeHtml(rx.formStrength)}</strong> on hold</p>
            <div class="form-group">
                <label for="hold-reason">Reason</label>
                <textarea id="hold-reason" class="form-input form-textarea" rows="2" placeholder="Enter reason (optional)..."></textarea>
            </div>`;
        const footer = `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                        <button class="btn btn-primary" id="confirm-hold-btn">Place on Hold</button>`;
        Components.showModal('Hold Prescription', body, footer);
        setTimeout(() => {
            document.getElementById('confirm-hold-btn')?.addEventListener('click', () => {
                const reason = document.getElementById('hold-reason')?.value;
                AppState.holdPrescription(rxId, reason);
                Components.closeModal();
                Components.showToast('Prescription placed on hold', 'success');
            });
        }, 50);
    }

    function _represcribe(rxId) {
        const rx = AppState.getPrescriptionById(rxId);
        if (!rx) return;
        const formData = {
            drugId: rx.drugId,
            drugName: rx.drugName,
            brandName: rx.brandName,
            formStrength: rx.formStrength,
            dosage: rx.dosage,
            frequency: rx.frequency,
            route: rx.route,
            quantity: rx.quantity,
            daysSupply: rx.daysSupply,
            refills: rx.refillsTotal,
            sig: rx.sig,
            daw: rx.daw,
            pharmacyId: rx.pharmacyId,
            priorAuth: rx.priorAuth,
            priorAuthNumber: rx.priorAuthNumber,
            note: 'Re-prescribed from ' + rx.id
        };
        AppState.set('prescribeFormData', formData);
        AppState.set('currentView', 'prescribe');
        AppState.notify();
    }

    // ==================== REFILL ACTIONS ====================
    function _showDenyRefillModal(rrId) {
        const reasons = AppState.get('denyReasons');
        const body = `
            <p>Select a reason for denying this refill request:</p>
            <div class="deny-reason-list">
                ${reasons.map((r, i) => `
                    <label class="radio-option">
                        <input type="radio" name="deny-reason" value="${Components.escapeAttr(r)}" ${i === 0 ? 'checked' : ''}>
                        <span>${Components.escapeHtml(r)}</span>
                    </label>
                `).join('')}
            </div>
            <div class="form-group" style="margin-top:12px">
                <label for="deny-notes">Additional Notes</label>
                <textarea id="deny-notes" class="form-input form-textarea" rows="2" placeholder="Optional notes..."></textarea>
            </div>`;
        const footer = `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                        <button class="btn btn-danger" id="confirm-deny-btn">Deny Request</button>`;
        Components.showModal('Deny Refill Request', body, footer);
        setTimeout(() => {
            document.getElementById('confirm-deny-btn')?.addEventListener('click', () => {
                const reason = document.querySelector('input[name="deny-reason"]:checked')?.value || 'Other';
                const notes = document.getElementById('deny-notes')?.value;
                AppState.denyRefillRequest(rrId, reason + (notes ? ': ' + notes : ''));
                Components.closeModal();
                Components.showToast('Refill request denied', 'success');
            });
        }, 50);
    }

    function _showModifyRefillModal(rrId) {
        const rr = AppState.get('refillRequests').find(r => r.id === rrId);
        if (!rr) return;
        const body = `
            <p>Modify and approve refill for <strong>${Components.escapeHtml(rr.drugName)}</strong></p>
            <div class="form-group">
                <label for="modify-refill-details">Modification Details <span class="required">*</span></label>
                <textarea id="modify-refill-details" class="form-input form-textarea" rows="3" placeholder="Describe the modifications (e.g., dose change, quantity change)..."></textarea>
            </div>`;
        const footer = `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                        <button class="btn btn-primary" id="confirm-modify-refill-btn">Modify & Approve</button>`;
        Components.showModal('Modify & Approve Refill', body, footer);
        setTimeout(() => {
            document.getElementById('confirm-modify-refill-btn')?.addEventListener('click', () => {
                const details = document.getElementById('modify-refill-details')?.value;
                if (!details) {
                    Components.showToast('Please enter modification details', 'error');
                    return;
                }
                AppState.modifyAndApproveRefillRequest(rrId, details);
                Components.closeModal();
                Components.showToast('Refill modified and approved', 'success');
            });
        }, 50);
    }

    // ==================== INTERACTION CHECKER ====================
    function _handleInteractionDrugSearch(query) {
        const results = AppState.searchDrugs(query);
        const container = document.getElementById('interaction-drug-search-results');
        if (!container) return;
        const currentDrugs = AppState.get('interactionCheckDrugs') || [];
        if (results.length === 0 && query.length >= 2) {
            container.innerHTML = '<div class="dropdown-item disabled">No drugs found</div>';
            container.classList.add('open');
            return;
        }
        if (results.length === 0) {
            container.classList.remove('open');
            return;
        }
        const filtered = results.filter(d => !currentDrugs.includes(d.id));
        container.innerHTML = filtered.slice(0, 15).map(d =>
            `<div class="dropdown-item drug-result" data-drug-id="${d.id}">
                <div class="drug-result-name">${Components.escapeHtml(d.genericName)} (${Components.escapeHtml(d.brandName)})</div>
            </div>`
        ).join('');
        container.classList.add('open');

        container.querySelectorAll('.drug-result').forEach(el => {
            el.addEventListener('click', (e) => {
                e.stopPropagation();
                const drugs = AppState.get('interactionCheckDrugs') || [];
                drugs.push(el.dataset.drugId);
                AppState.set('interactionCheckDrugs', drugs);
                container.classList.remove('open');
                const input = document.getElementById('interaction-drug-input');
                if (input) input.value = '';
                _render();
            });
        });
    }

    function _removeInteractionDrug(drugId) {
        const drugs = AppState.get('interactionCheckDrugs') || [];
        const idx = drugs.indexOf(drugId);
        if (idx >= 0) drugs.splice(idx, 1);
        AppState.set('interactionCheckDrugs', drugs);
        _render();
    }

    function _loadPatientMedsForInteractionCheck() {
        const activeDrugIds = AppState.getActivePatientDrugIds();
        AppState.set('interactionCheckDrugs', activeDrugIds);
        _render();
        Components.showToast(`Loaded ${activeDrugIds.length} active medications`, 'success');
    }

    // ==================== SETTINGS ====================
    function _saveSettings() {
        const settings = AppState.get('settings');
        const daysSupplyInput = document.getElementById('setting-days-supply');
        if (daysSupplyInput) settings.defaultDaysSupply = parseInt(daysSupplyInput.value) || 30;
        const refillsInput = document.getElementById('setting-refills');
        if (refillsInput) settings.defaultRefills = parseInt(refillsInput.value) || 0;

        // Toggle values are handled by the toggle handler, but read current states
        const erxToggle = document.getElementById('setting-erx');
        if (erxToggle) settings.eRxEnabled = erxToggle.classList.contains('active');
        const genericToggle = document.getElementById('setting-generic-first');
        if (genericToggle) settings.showGenericFirst = genericToggle.classList.contains('active');
        const interactionsToggle = document.getElementById('setting-auto-interactions');
        if (interactionsToggle) settings.autoCheckInteractions = interactionsToggle.classList.contains('active');
        const allergyToggle = document.getElementById('setting-allergy-review');
        if (allergyToggle) settings.requireAllergyReview = allergyToggle.classList.contains('active');
        const sigToggle = document.getElementById('setting-signature');
        if (sigToggle) settings.signatureRequired = sigToggle.classList.contains('active');

        AppState.updateSettings(settings);
        Components.showToast('Settings saved successfully', 'success');
    }

    // ==================== TOGGLE HANDLER ====================
    function _handleToggle(toggleId, isActive) {
        switch (toggleId) {
            case 'daw-toggle':
                _updatePrescribeFormData('daw', isActive);
                break;
            case 'prior-auth-toggle':
                _updatePrescribeFormData('priorAuth', isActive);
                break;
            // Settings toggles are read on save
        }
    }

    return { init };
})();

document.addEventListener('DOMContentLoaded', App.init);
