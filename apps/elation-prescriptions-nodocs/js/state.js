/* Elation Prescriptions — State Management */
const AppState = (function() {
    let _listeners = [];
    let _state = {};

    function _deepClone(obj) {
        return JSON.parse(JSON.stringify(obj));
    }

    function init() {
        const saved = localStorage.getItem('elationPrescriptionsState');
        if (saved) {
            try {
                const parsed = JSON.parse(saved);
                if (parsed._seedVersion === SEED_DATA_VERSION) {
                    _state = parsed;
                    _state.currentView = 'medications';
                    _state.currentPrescriptionId = null;
                    _state.prescribeFormData = null;
                    _state.interactionCheckDrugs = [];
                    _state.searchQuery = '';
                    _state.medicationFilter = 'active';
                    _state.medicationSort = 'name-asc';
                    _state.historyFilter = { dateFrom: '', dateTo: '', medication: '', provider: '' };
                    _state.refillFilter = 'pending';
                    _state.currentPage = 1;
                    _state.pageSize = 20;
                    notify();
                    return;
                }
            } catch (e) { /* fall through to seed */ }
        }
        _loadSeedData();
        notify();
    }

    function _loadSeedData() {
        _state = {
            _seedVersion: SEED_DATA_VERSION,
            patients: _deepClone(PATIENTS),
            currentPatientId: CURRENT_PATIENT_ID,
            providers: _deepClone(PROVIDERS),
            currentProviderId: CURRENT_USER_PROVIDER_ID,
            pharmacies: _deepClone(PHARMACIES),
            drugCatalog: _deepClone(DRUG_CATALOG),
            drugInteractions: _deepClone(DRUG_INTERACTIONS),
            prescriptions: _deepClone(PRESCRIPTIONS),
            refillRequests: _deepClone(REFILL_REQUESTS),
            settings: _deepClone(DEFAULT_SETTINGS),
            denyReasons: _deepClone(DENY_REASONS),
            _nextRxId: 31,
            _nextRrId: 13,

            // UI state (not persisted)
            currentView: 'medications',
            currentPrescriptionId: null,
            prescribeFormData: null,
            interactionCheckDrugs: [],
            searchQuery: '',
            medicationFilter: 'active',
            medicationSort: 'name-asc',
            historyFilter: { dateFrom: '', dateTo: '', medication: '', provider: '' },
            refillFilter: 'pending',
            currentPage: 1,
            pageSize: 20
        };
    }

    function getSerializableState() {
        return {
            _seedVersion: _state._seedVersion,
            patients: _state.patients,
            currentPatientId: _state.currentPatientId,
            providers: _state.providers,
            currentProviderId: _state.currentProviderId,
            pharmacies: _state.pharmacies,
            drugCatalog: _state.drugCatalog,
            drugInteractions: _state.drugInteractions,
            prescriptions: _state.prescriptions,
            refillRequests: _state.refillRequests,
            settings: _state.settings,
            denyReasons: _state.denyReasons,
            _nextRxId: _state._nextRxId,
            _nextRrId: _state._nextRrId
        };
    }

    function _persist() {
        localStorage.setItem('elationPrescriptionsState', JSON.stringify(getSerializableState()));
    }

    function _pushStateToServer() {
        try {
            fetch('/api/state', {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(getSerializableState())
            });
        } catch (e) { /* ignore */ }
    }

    function notify() {
        _persist();
        _pushStateToServer();
        _listeners.forEach(fn => fn(_state));
    }

    function subscribe(fn) {
        _listeners.push(fn);
    }

    function get(key) {
        return _state[key];
    }

    function set(key, value) {
        _state[key] = value;
    }

    function setUI(key, value) {
        _state[key] = value;
        _listeners.forEach(fn => fn(_state));
    }

    // --- Patient Helpers ---
    function getCurrentPatient() {
        return _state.patients.find(p => p.id === _state.currentPatientId);
    }

    function switchPatient(patientId) {
        _state.currentPatientId = patientId;
        _state.currentView = 'medications';
        _state.currentPrescriptionId = null;
        _state.searchQuery = '';
        _state.medicationFilter = 'active';
        _state.currentPage = 1;
        notify();
    }

    // --- Provider Helpers ---
    function getCurrentProvider() {
        return _state.providers.find(p => p.id === _state.currentProviderId);
    }

    function getProviderById(id) {
        return _state.providers.find(p => p.id === id);
    }

    // --- Pharmacy Helpers ---
    function getPharmacyById(id) {
        return _state.pharmacies.find(p => p.id === id);
    }

    // --- Drug Helpers ---
    function getDrugById(id) {
        return _state.drugCatalog.find(d => d.id === id);
    }

    function searchDrugs(query) {
        if (!query || query.length < 2) return [];
        const q = query.toLowerCase();
        return _state.drugCatalog.filter(d =>
            d.brandName.toLowerCase().includes(q) ||
            d.genericName.toLowerCase().includes(q) ||
            d.drugClass.toLowerCase().includes(q)
        );
    }

    // --- Prescription Helpers ---
    function getPatientPrescriptions(patientId) {
        patientId = patientId || _state.currentPatientId;
        return _state.prescriptions.filter(rx => rx.patientId === patientId);
    }

    function getFilteredPrescriptions() {
        let rxs = getPatientPrescriptions();
        const filter = _state.medicationFilter;
        if (filter === 'active') {
            rxs = rxs.filter(rx => rx.status === 'active' || rx.status === 'on-hold');
        } else if (filter === 'discontinued') {
            rxs = rxs.filter(rx => rx.status === 'discontinued');
        } else if (filter === 'completed') {
            rxs = rxs.filter(rx => rx.status === 'completed');
        }
        // filter !== 'all' already handled above

        if (_state.searchQuery) {
            const q = _state.searchQuery.toLowerCase();
            rxs = rxs.filter(rx =>
                rx.drugName.toLowerCase().includes(q) ||
                rx.brandName.toLowerCase().includes(q) ||
                rx.formStrength.toLowerCase().includes(q)
            );
        }

        const sort = _state.medicationSort;
        rxs.sort((a, b) => {
            if (sort === 'name-asc') return a.drugName.localeCompare(b.drugName);
            if (sort === 'name-desc') return b.drugName.localeCompare(a.drugName);
            if (sort === 'date-asc') return a.startDate.localeCompare(b.startDate);
            if (sort === 'date-desc') return b.startDate.localeCompare(a.startDate);
            if (sort === 'status') return a.status.localeCompare(b.status);
            return 0;
        });

        return rxs;
    }

    function getPrescriptionById(id) {
        return _state.prescriptions.find(rx => rx.id === id);
    }

    function createPrescription(data) {
        const id = 'rx_' + String(_state._nextRxId).padStart(3, '0');
        _state._nextRxId++;
        const now = new Date().toISOString().split('T')[0];
        const provider = getCurrentProvider();
        const providerName = provider ? `${provider.title === 'MD' || provider.title === 'DO' ? 'Dr. ' : ''}${provider.firstName} ${provider.lastName}${provider.title !== 'MD' && provider.title !== 'DO' ? ', ' + provider.title : ''}` : 'Unknown';

        const rx = {
            id: id,
            patientId: _state.currentPatientId,
            drugId: data.drugId,
            drugName: data.drugName,
            brandName: data.brandName,
            formStrength: data.formStrength,
            dosage: data.dosage,
            frequency: data.frequency,
            route: data.route,
            quantity: parseInt(data.quantity) || 0,
            daysSupply: parseInt(data.daysSupply) || 0,
            refillsTotal: parseInt(data.refills) || 0,
            refillsRemaining: parseInt(data.refills) || 0,
            sig: data.sig,
            daw: data.daw || false,
            pharmacyId: data.pharmacyId,
            prescriberId: _state.currentProviderId,
            status: 'active',
            startDate: now,
            endDate: null,
            priorAuth: data.priorAuth || false,
            priorAuthNumber: data.priorAuthNumber || null,
            discontinuedReason: null,
            discontinuedDate: null,
            fillHistory: [],
            history: [
                { action: 'prescribed', date: now, provider: providerName, note: data.note || 'New prescription' }
            ]
        };
        _state.prescriptions.push(rx);
        notify();
        return rx;
    }

    function renewPrescription(rxId, refills) {
        const rx = getPrescriptionById(rxId);
        if (!rx) return;
        const now = new Date().toISOString().split('T')[0];
        const provider = getCurrentProvider();
        const providerName = provider ? `${provider.title === 'MD' || provider.title === 'DO' ? 'Dr. ' : ''}${provider.firstName} ${provider.lastName}${provider.title !== 'MD' && provider.title !== 'DO' ? ', ' + provider.title : ''}` : 'Unknown';
        rx.refillsRemaining = parseInt(refills) || rx.refillsTotal;
        rx.refillsTotal = rx.refillsRemaining;
        rx.status = 'active';
        rx.history.push({ action: 'renewed', date: now, provider: providerName, note: `Renewed with ${rx.refillsRemaining} refills` });
        notify();
    }

    function modifyPrescription(rxId, changes) {
        const rx = getPrescriptionById(rxId);
        if (!rx) return;
        const now = new Date().toISOString().split('T')[0];
        const provider = getCurrentProvider();
        const providerName = provider ? `${provider.title === 'MD' || provider.title === 'DO' ? 'Dr. ' : ''}${provider.firstName} ${provider.lastName}${provider.title !== 'MD' && provider.title !== 'DO' ? ', ' + provider.title : ''}` : 'Unknown';
        const changeSummary = [];
        for (const key of Object.keys(changes)) {
            if (rx[key] !== changes[key]) {
                changeSummary.push(`${key}: ${rx[key]} → ${changes[key]}`);
                rx[key] = changes[key];
            }
        }
        if (changeSummary.length > 0) {
            rx.history.push({ action: 'modified', date: now, provider: providerName, note: changeSummary.join('; ') });
        }
        notify();
    }

    function discontinuePrescription(rxId, reason) {
        const rx = getPrescriptionById(rxId);
        if (!rx) return;
        const now = new Date().toISOString().split('T')[0];
        const provider = getCurrentProvider();
        const providerName = provider ? `${provider.title === 'MD' || provider.title === 'DO' ? 'Dr. ' : ''}${provider.firstName} ${provider.lastName}${provider.title !== 'MD' && provider.title !== 'DO' ? ', ' + provider.title : ''}` : 'Unknown';
        rx.status = 'discontinued';
        rx.discontinuedReason = reason;
        rx.discontinuedDate = now;
        rx.endDate = now;
        rx.history.push({ action: 'discontinued', date: now, provider: providerName, note: reason });
        notify();
    }

    function holdPrescription(rxId, reason) {
        const rx = getPrescriptionById(rxId);
        if (!rx) return;
        const now = new Date().toISOString().split('T')[0];
        const provider = getCurrentProvider();
        const providerName = provider ? `${provider.title === 'MD' || provider.title === 'DO' ? 'Dr. ' : ''}${provider.firstName} ${provider.lastName}${provider.title !== 'MD' && provider.title !== 'DO' ? ', ' + provider.title : ''}` : 'Unknown';
        rx.status = 'on-hold';
        rx.history.push({ action: 'on-hold', date: now, provider: providerName, note: reason || 'Placed on hold' });
        notify();
    }

    function resumePrescription(rxId) {
        const rx = getPrescriptionById(rxId);
        if (!rx) return;
        const now = new Date().toISOString().split('T')[0];
        const provider = getCurrentProvider();
        const providerName = provider ? `${provider.title === 'MD' || provider.title === 'DO' ? 'Dr. ' : ''}${provider.firstName} ${provider.lastName}${provider.title !== 'MD' && provider.title !== 'DO' ? ', ' + provider.title : ''}` : 'Unknown';
        rx.status = 'active';
        rx.history.push({ action: 'resumed', date: now, provider: providerName, note: 'Resumed from hold' });
        notify();
    }

    function cancelPrescription(rxId) {
        const rx = getPrescriptionById(rxId);
        if (!rx) return;
        const now = new Date().toISOString().split('T')[0];
        const provider = getCurrentProvider();
        const providerName = provider ? `${provider.title === 'MD' || provider.title === 'DO' ? 'Dr. ' : ''}${provider.firstName} ${provider.lastName}${provider.title !== 'MD' && provider.title !== 'DO' ? ', ' + provider.title : ''}` : 'Unknown';
        rx.status = 'cancelled';
        rx.endDate = now;
        rx.history.push({ action: 'cancelled', date: now, provider: providerName, note: 'Prescription cancelled' });
        notify();
    }

    // --- Refill Request Helpers ---
    function getRefillRequests(filter) {
        filter = filter || _state.refillFilter;
        let requests = _state.refillRequests.slice();
        if (filter && filter !== 'all') {
            requests = requests.filter(r => r.status === filter);
        }
        requests.sort((a, b) => {
            if (a.urgency === 'urgent' && b.urgency !== 'urgent') return -1;
            if (b.urgency === 'urgent' && a.urgency !== 'urgent') return 1;
            return new Date(b.requestDate) - new Date(a.requestDate);
        });
        return requests;
    }

    function getPendingRefillCount() {
        return _state.refillRequests.filter(r => r.status === 'pending').length;
    }

    function approveRefillRequest(rrId) {
        const rr = _state.refillRequests.find(r => r.id === rrId);
        if (!rr) return;
        rr.status = 'approved';
        rr.responseDate = new Date().toISOString();
        rr.respondedBy = _state.currentProviderId;
        // also update the prescription refills
        const rx = getPrescriptionById(rr.prescriptionId);
        if (rx && rx.refillsRemaining > 0) {
            rx.refillsRemaining--;
            const now = new Date().toISOString().split('T')[0];
            rx.fillHistory.push({
                fillDate: now,
                pharmacy: rr.pharmacyName,
                quantity: rx.quantity,
                daysSupply: rx.daysSupply,
                fillNumber: rx.fillHistory.length + 1
            });
            rx.history.push({ action: 'refill-approved', date: now, provider: getCurrentProvider() ? `Dr. ${getCurrentProvider().lastName}` : 'Provider', note: 'Refill request approved' });
        }
        notify();
    }

    function denyRefillRequest(rrId, reason) {
        const rr = _state.refillRequests.find(r => r.id === rrId);
        if (!rr) return;
        rr.status = 'denied';
        rr.denyReason = reason;
        rr.responseDate = new Date().toISOString();
        rr.respondedBy = _state.currentProviderId;
        notify();
    }

    function modifyAndApproveRefillRequest(rrId, modifications) {
        const rr = _state.refillRequests.find(r => r.id === rrId);
        if (!rr) return;
        rr.status = 'modified';
        rr.responseDate = new Date().toISOString();
        rr.respondedBy = _state.currentProviderId;
        rr.modifiedDetails = modifications;
        notify();
    }

    // --- Drug Interaction Helpers ---
    function checkInteractions(drugIds) {
        const interactions = [];
        for (let i = 0; i < drugIds.length; i++) {
            for (let j = i + 1; j < drugIds.length; j++) {
                const d1 = drugIds[i], d2 = drugIds[j];
                const found = _state.drugInteractions.filter(int =>
                    (int.drug1Id === d1 && int.drug2Id === d2) ||
                    (int.drug1Id === d2 && int.drug2Id === d1)
                );
                interactions.push(...found);
            }
        }
        return interactions;
    }

    function checkAllergyConflicts(drugId) {
        const drug = getDrugById(drugId);
        if (!drug) return [];
        const patient = getCurrentPatient();
        if (!patient) return [];
        const conflicts = [];
        for (const allergy of patient.allergies) {
            if (drug.allergenCrossReactivity.includes(allergy.substance)) {
                conflicts.push({
                    drug: drug.genericName,
                    allergen: allergy.substance,
                    reaction: allergy.reaction,
                    severity: allergy.severity
                });
            }
        }
        return conflicts;
    }

    function getActivePatientDrugIds() {
        const rxs = getPatientPrescriptions();
        return rxs.filter(rx => rx.status === 'active').map(rx => rx.drugId);
    }

    // --- Medication History ---
    function getMedicationHistory() {
        let rxs = getPatientPrescriptions();
        const f = _state.historyFilter;
        if (f.dateFrom) {
            rxs = rxs.filter(rx => rx.startDate >= f.dateFrom);
        }
        if (f.dateTo) {
            rxs = rxs.filter(rx => rx.startDate <= f.dateTo);
        }
        if (f.medication) {
            const q = f.medication.toLowerCase();
            rxs = rxs.filter(rx => rx.drugName.toLowerCase().includes(q) || rx.brandName.toLowerCase().includes(q));
        }
        if (f.provider) {
            rxs = rxs.filter(rx => rx.prescriberId === f.provider);
        }
        rxs.sort((a, b) => b.startDate.localeCompare(a.startDate));
        return rxs;
    }

    // --- Settings ---
    function updateSettings(changes) {
        Object.assign(_state.settings, changes);
        notify();
    }

    function toggleFavoriteDrug(drugId) {
        const idx = _state.settings.favoritesDrugIds.indexOf(drugId);
        if (idx >= 0) {
            _state.settings.favoritesDrugIds.splice(idx, 1);
        } else {
            _state.settings.favoritesDrugIds.push(drugId);
        }
        notify();
    }

    function isFavoriteDrug(drugId) {
        return _state.settings.favoritesDrugIds.includes(drugId);
    }

    // --- Reset ---
    function resetToSeedData() {
        localStorage.removeItem('elationPrescriptionsState');
        _loadSeedData();
        notify();
    }

    return {
        init, subscribe, get, set, setUI, notify, getSerializableState, resetToSeedData,
        getCurrentPatient, switchPatient,
        getCurrentProvider, getProviderById,
        getPharmacyById,
        getDrugById, searchDrugs,
        getPatientPrescriptions, getFilteredPrescriptions, getPrescriptionById,
        createPrescription, renewPrescription, modifyPrescription,
        discontinuePrescription, holdPrescription, resumePrescription, cancelPrescription,
        getRefillRequests, getPendingRefillCount, approveRefillRequest, denyRefillRequest, modifyAndApproveRefillRequest,
        checkInteractions, checkAllergyConflicts, getActivePatientDrugIds,
        getMedicationHistory,
        updateSettings, toggleFavoriteDrug, isFavoriteDrug
    };
})();
