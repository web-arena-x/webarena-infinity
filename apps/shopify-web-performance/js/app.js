// ============================================================
// app.js — Router and application initialization
// ============================================================

const Router = {
    routes: {
        '/': () => Views.home(),
        '/themes': () => Views.themes(),
        '/themes/:id': (params) => Views.themeDetail(params.id),
        '/apps': () => Views.apps(),
        '/apps/:id': (params) => Views.appDetail(params.id),
        '/reports': () => Views.reports(),
        '/reports/:type/:metric': (params) => Views.reportDetail(params.type, params.metric),
        '/pages': () => Views.pages(),
        '/pages/:id': (params) => Views.pageDetail(params.id),
        '/optimizations': () => Views.optimizations(),
        '/alerts': () => Views.alerts(),
        '/events': () => Views.events(),
        '/settings': () => Views.settings()
    },

    navigate(path, skipHistory = false) {
        const [basePath, queryString] = path.split('?');
        const params = {};
        if (queryString) {
            queryString.split('&').forEach(p => {
                const [k, v] = p.split('=');
                params[k] = decodeURIComponent(v);
            });
        }

        AppState.routeParams = params;
        AppState.currentRoute = basePath;

        if (!skipHistory) {
            history.pushState({ path }, '', `#${path}`);
        }

        Router.render();
    },

    refresh() {
        Router.render();
    },

    render() {
        const path = AppState.currentRoute;
        const contentWrapper = document.getElementById('contentWrapper');

        let html = null;
        for (const [pattern, handler] of Object.entries(Router.routes)) {
            const match = Router.matchRoute(pattern, path);
            if (match !== null) {
                html = handler(match);
                break;
            }
        }

        if (html === null) {
            html = Views._notFound('Page not found');
        }

        contentWrapper.innerHTML = html;

        // Update active sidebar item
        document.querySelectorAll('.sidebar-item').forEach(item => {
            const route = item.getAttribute('data-route');
            if (route === path || (route !== '/' && path.startsWith(route))) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });

        // Attach event handlers for dynamic content
        Router.attachHandlers();
    },

    matchRoute(pattern, path) {
        const patternParts = pattern.split('/');
        const pathParts = path.split('/');

        if (patternParts.length !== pathParts.length) return null;

        const params = {};
        for (let i = 0; i < patternParts.length; i++) {
            if (patternParts[i].startsWith(':')) {
                params[patternParts[i].substring(1)] = pathParts[i];
            } else if (patternParts[i] !== pathParts[i]) {
                return null;
            }
        }
        return params;
    },

    attachHandlers() {
        // Route links
        document.querySelectorAll('[data-route]').forEach(el => {
            if (el._routeHandlerAttached) return;
            el._routeHandlerAttached = true;
            el.addEventListener('click', (e) => {
                e.preventDefault();
                const route = el.getAttribute('data-route');
                Router.navigate(route);
            });
        });

        // Tab items
        document.querySelectorAll('.tab-item').forEach(el => {
            if (el._tabHandlerAttached) return;
            el._tabHandlerAttached = true;
            el.addEventListener('click', () => {
                const tab = el.getAttribute('data-tab');
                const currentPath = AppState.currentRoute;
                Router.navigate(`${currentPath}?tab=${tab}`);
            });
        });

        // ---- Sidebar toggle ----
        const sidebarToggle = document.getElementById('sidebarToggle');
        if (sidebarToggle && !sidebarToggle._attached) {
            sidebarToggle._attached = true;
            sidebarToggle.addEventListener('click', () => {
                const sidebar = document.getElementById('sidebar');
                sidebar.classList.toggle('collapsed');
                AppState.sidebarOpen = !sidebar.classList.contains('collapsed');
            });
        }

        // ---- User menu ----
        const userMenu = document.getElementById('userMenu');
        if (userMenu && !userMenu._attached) {
            userMenu._attached = true;
            const avatar = document.getElementById('currentUserAvatar');
            avatar.textContent = AppState.currentUser.name.split(' ').map(n => n[0]).join('');
            avatar.style.backgroundColor = AppState.currentUser.avatarColor;

            const header = document.getElementById('userDropdownHeader');
            header.innerHTML = `<strong>${Components.escapeHtml(AppState.currentUser.name)}</strong><br><span class="text-small text-muted">${Components.escapeHtml(AppState.currentUser.email)}</span>`;

            avatar.addEventListener('click', (e) => {
                e.stopPropagation();
                document.getElementById('userDropdown').classList.toggle('open');
            });

            document.addEventListener('click', () => {
                document.getElementById('userDropdown').classList.remove('open');
            });
        }

        // ---- Action buttons ----

        // Activate theme
        document.querySelectorAll('[data-action="activate-theme"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const themeId = parseInt(btn.getAttribute('data-theme-id'));
                const theme = AppState.getThemeById(themeId);
                Components.confirm('Activate Theme', `Are you sure you want to activate "${theme.name}"? This will replace your current active theme.`, () => {
                    AppState.activateTheme(themeId);
                    Components.showToast(`Theme "${theme.name}" activated`, 'success');
                    Router.refresh();
                });
            });
        });

        // Save theme settings
        const saveThemeBtn = document.getElementById('saveThemeSettingsBtn');
        if (saveThemeBtn && !saveThemeBtn._attached) {
            saveThemeBtn._attached = true;
            saveThemeBtn.addEventListener('click', () => {
                const themeId = parseInt(AppState.currentRoute.split('/').pop());
                const settings = {
                    pageTransitions: document.getElementById('pageTransitions')?.checked || false,
                    lazyLoading: document.getElementById('lazyLoading')?.checked || false,
                    stickyHeader: document.getElementById('stickyHeader')?.checked || false,
                    predictiveSearch: document.getElementById('predictiveSearch')?.checked || false,
                    animationsEnabled: document.getElementById('animationsEnabled')?.checked || false,
                    cartType: document.getElementById('cartTypeDropdown')?.getAttribute('data-value') || 'drawer',
                    paginationLimit: parseInt(document.getElementById('paginationLimit')?.value) || 24
                };
                AppState.updateThemeSettings(themeId, settings);
                Components.showToast('Theme settings saved', 'success');
                Router.refresh();
            });
        }

        // Install/uninstall app
        document.querySelectorAll('[data-action="install-app"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const appId = parseInt(btn.getAttribute('data-app-id'));
                const app = AppState.getAppById(appId);
                AppState.installApp(appId);
                Components.showToast(`"${app.name}" installed`, 'success');
                Router.refresh();
            });
        });

        document.querySelectorAll('[data-action="uninstall-app"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const appId = parseInt(btn.getAttribute('data-app-id'));
                const app = AppState.getAppById(appId);
                Components.confirm('Uninstall App', `Are you sure you want to uninstall "${app.name}"? This may improve your store's performance.`, () => {
                    AppState.uninstallApp(appId);
                    Components.showToast(`"${app.name}" uninstalled`, 'success');
                    Router.navigate('/apps');
                }, { type: 'danger', confirmText: 'Uninstall' });
            });
        });

        // Save app settings
        const saveAppBtn = document.getElementById('saveAppSettingsBtn');
        if (saveAppBtn && !saveAppBtn._attached) {
            saveAppBtn._attached = true;
            saveAppBtn.addEventListener('click', () => {
                const appId = parseInt(AppState.currentRoute.split('/').pop());
                const app = AppState.getAppById(appId);
                if (!app) return;

                const settings = {};
                for (const [key, value] of Object.entries(app.settings)) {
                    const el = document.getElementById(`appSetting_${key}`);
                    if (!el) continue;
                    if (typeof value === 'boolean') {
                        settings[key] = el.checked;
                    } else if (typeof value === 'number') {
                        settings[key] = parseInt(el.value) || 0;
                    } else {
                        settings[key] = el.value;
                    }
                }
                AppState.updateAppSettings(appId, settings);
                Components.showToast('App settings saved', 'success');
                Router.refresh();
            });
        }

        // Toggle page monitoring
        document.querySelectorAll('[data-action="toggle-monitoring"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const pageId = parseInt(btn.getAttribute('data-page-id'));
                AppState.togglePageMonitoring(pageId);
                const page = AppState.getPageById(pageId);
                Components.showToast(`Monitoring ${page.monitored ? 'resumed' : 'paused'} for "${page.name}"`, 'success');
                Router.refresh();
            });
        });

        // Remove page
        document.querySelectorAll('[data-action="remove-page"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const pageId = parseInt(btn.getAttribute('data-page-id'));
                const page = AppState.getPageById(pageId);
                Components.confirm('Remove Page', `Are you sure you want to remove "${page.name}" from monitoring?`, () => {
                    AppState.removePage(pageId);
                    Components.showToast('Page removed', 'success');
                    Router.refresh();
                }, { type: 'danger', confirmText: 'Remove' });
            });
        });

        // Add page button
        const addPageBtn = document.getElementById('addPageBtn');
        if (addPageBtn && !addPageBtn._attached) {
            addPageBtn._attached = true;
            addPageBtn.addEventListener('click', () => Views._showAddPageModal());
        }

        // Add event button
        const addEventBtn = document.getElementById('addEventBtn');
        if (addEventBtn && !addEventBtn._attached) {
            addEventBtn._attached = true;
            addEventBtn.addEventListener('click', () => Views._showAddEventModal());
        }

        // Event actions (edit/remove)
        document.querySelectorAll('[data-action="edit-event"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const eventId = parseInt(btn.getAttribute('data-event-id'));
                Views._showEditEventModal(eventId);
            });
        });

        document.querySelectorAll('[data-action="remove-event"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const eventId = parseInt(btn.getAttribute('data-event-id'));
                Components.confirm('Remove Event', 'Are you sure you want to remove this event?', () => {
                    AppState.removeEvent(eventId);
                    Components.showToast('Event removed', 'success');
                    Router.refresh();
                }, { type: 'danger', confirmText: 'Remove' });
            });
        });

        // Add alert button
        const addAlertBtn = document.getElementById('addAlertBtn');
        if (addAlertBtn && !addAlertBtn._attached) {
            addAlertBtn._attached = true;
            addAlertBtn.addEventListener('click', () => Views._showAddAlertModal());
        }

        // Alert actions
        document.querySelectorAll('[data-action="toggle-alert"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const alertId = parseInt(btn.getAttribute('data-alert-id'));
                AppState.toggleAlertRule(alertId);
                const rule = AppState.getAlertById(alertId);
                Components.showToast(`Alert "${rule.name}" ${rule.enabled ? 'enabled' : 'disabled'}`, 'success');
                Router.refresh();
            });
        });

        document.querySelectorAll('[data-action="edit-alert"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const alertId = parseInt(btn.getAttribute('data-alert-id'));
                Views._showEditAlertModal(alertId);
            });
        });

        document.querySelectorAll('[data-action="remove-alert"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const alertId = parseInt(btn.getAttribute('data-alert-id'));
                Components.confirm('Remove Alert', 'Are you sure you want to remove this alert rule?', () => {
                    AppState.removeAlertRule(alertId);
                    Components.showToast('Alert rule removed', 'success');
                    Router.refresh();
                }, { type: 'danger', confirmText: 'Remove' });
            });
        });

        // Add optimization button
        const addOptBtn = document.getElementById('addOptimizationBtn');
        if (addOptBtn && !addOptBtn._attached) {
            addOptBtn._attached = true;
            addOptBtn.addEventListener('click', () => Views._showAddOptimizationModal());
        }

        // Optimization actions
        document.querySelectorAll('[data-action="start-optimization"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const optId = parseInt(btn.getAttribute('data-opt-id'));
                AppState.updateOptimization(optId, { status: 'in_progress' });
                Components.showToast('Optimization started', 'success');
                Router.refresh();
            });
        });

        document.querySelectorAll('[data-action="complete-optimization"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const optId = parseInt(btn.getAttribute('data-opt-id'));
                AppState.updateOptimization(optId, { status: 'completed' });
                Components.showToast('Optimization completed', 'success');
                Router.refresh();
            });
        });

        document.querySelectorAll('[data-action="dismiss-optimization"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const optId = parseInt(btn.getAttribute('data-opt-id'));
                AppState.updateOptimization(optId, { status: 'dismissed' });
                Components.showToast('Optimization dismissed', 'success');
                Router.refresh();
            });
        });

        document.querySelectorAll('[data-action="remove-optimization"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const optId = parseInt(btn.getAttribute('data-opt-id'));
                Components.confirm('Remove Optimization', 'Are you sure you want to remove this optimization?', () => {
                    AppState.removeOptimization(optId);
                    Components.showToast('Optimization removed', 'success');
                    Router.refresh();
                }, { type: 'danger', confirmText: 'Remove' });
            });
        });

        // Create report button
        const createReportBtn = document.getElementById('createReportBtn');
        if (createReportBtn && !createReportBtn._attached) {
            createReportBtn._attached = true;
            createReportBtn.addEventListener('click', () => Views._showCreateReportModal());
        }

        // Delete saved report
        document.querySelectorAll('[data-action="delete-report"]').forEach(btn => {
            if (btn._attached) return;
            btn._attached = true;
            btn.addEventListener('click', () => {
                const reportId = parseInt(btn.getAttribute('data-report-id'));
                Components.confirm('Delete Report', 'Are you sure you want to delete this saved report?', () => {
                    AppState.removeSavedReport(reportId);
                    Components.showToast('Report deleted', 'success');
                    Router.refresh();
                }, { type: 'danger', confirmText: 'Delete' });
            });
        });

        // Save store settings
        const saveStoreBtn = document.getElementById('saveStoreSettingsBtn');
        if (saveStoreBtn && !saveStoreBtn._attached) {
            saveStoreBtn._attached = true;
            saveStoreBtn.addEventListener('click', () => {
                const name = document.getElementById('storeName')?.value?.trim();
                const domain = document.getElementById('storeDomain')?.value?.trim();
                const passwordProtected = document.getElementById('passwordProtected')?.checked || false;

                if (!name) {
                    Components.showToast('Store name is required', 'error');
                    return;
                }

                AppState.updateStore({ name, domain, passwordProtected });
                Components.showToast('Store settings saved', 'success');
                Router.refresh();
            });
        }

        // Save performance budgets
        const saveBudgetsBtn = document.getElementById('saveBudgetsBtn');
        if (saveBudgetsBtn && !saveBudgetsBtn._attached) {
            saveBudgetsBtn._attached = true;
            saveBudgetsBtn.addEventListener('click', () => {
                const lcpTarget = parseFloat(document.getElementById('lcpTarget')?.value);
                const lcpWarning = parseFloat(document.getElementById('lcpWarning')?.value);
                const inpTarget = parseFloat(document.getElementById('inpTarget')?.value);
                const inpWarning = parseFloat(document.getElementById('inpWarning')?.value);
                const clsTarget = parseFloat(document.getElementById('clsTarget')?.value);
                const clsWarning = parseFloat(document.getElementById('clsWarning')?.value);

                if (isNaN(lcpTarget) || isNaN(lcpWarning) || isNaN(inpTarget) || isNaN(inpWarning) || isNaN(clsTarget) || isNaN(clsWarning)) {
                    Components.showToast('Please fill in all budget values', 'error');
                    return;
                }

                AppState.updateBudget('lcp', { target: lcpTarget, warning: lcpWarning });
                AppState.updateBudget('inp', { target: inpTarget, warning: inpWarning });
                AppState.updateBudget('cls', { target: clsTarget, warning: clsWarning });
                Components.showToast('Performance budgets saved', 'success');
                Router.refresh();
            });
        }

        // Save page settings
        const savePageBtn = document.getElementById('savePageSettingsBtn');
        if (savePageBtn && !savePageBtn._attached) {
            savePageBtn._attached = true;
            savePageBtn.addEventListener('click', () => {
                const pageId = parseInt(AppState.currentRoute.split('/').pop());
                const name = document.getElementById('pageName')?.value?.trim();
                const path = document.getElementById('pagePath')?.value?.trim();
                const type = document.getElementById('pageTypeDropdown')?.getAttribute('data-value');
                const priority = document.getElementById('pagePriorityDropdown')?.getAttribute('data-value');

                if (!name || !path) {
                    Components.showToast('Name and path are required', 'error');
                    return;
                }

                AppState.updatePage(pageId, { name, path, type, priority });
                Components.showToast('Page settings saved', 'success');
                Router.refresh();
            });
        }

        // Reset data button
        const resetBtn = document.getElementById('resetDataBtn');
        if (resetBtn && !resetBtn._attached) {
            resetBtn._attached = true;
            resetBtn.addEventListener('click', () => {
                Components.confirm('Reset All Data', 'This will restore all settings, apps, themes, and reports to their default values. This cannot be undone.', () => {
                    AppState.resetToSeedData();
                    Components.showToast('All data has been reset to defaults', 'success');
                    Router.navigate('/');
                }, { type: 'danger', confirmText: 'Reset Everything' });
            });
        }

        // Report filter dropdowns
        const dateRangeFilter = document.getElementById('dateRangeFilter');
        if (dateRangeFilter && !dateRangeFilter._attached) {
            dateRangeFilter._attached = true;
            dateRangeFilter.addEventListener('change', (e) => {
                const dateRange = e.detail.value;
                const deviceType = document.getElementById('deviceTypeFilter')?.getAttribute('data-value') || 'all';
                const currentPath = AppState.currentRoute;
                Router.navigate(`${currentPath}?dateRange=${dateRange}&deviceType=${deviceType}`);
            });
        }

        const deviceTypeFilter = document.getElementById('deviceTypeFilter');
        if (deviceTypeFilter && !deviceTypeFilter._attached) {
            deviceTypeFilter._attached = true;
            deviceTypeFilter.addEventListener('change', (e) => {
                const deviceType = e.detail.value;
                const dateRange = document.getElementById('dateRangeFilter')?.getAttribute('data-value') || 'last_30_days';
                const currentPath = AppState.currentRoute;
                Router.navigate(`${currentPath}?dateRange=${dateRange}&deviceType=${deviceType}`);
            });
        }
    }
};

// ---- SSE listener for reset events ----
function initSSE() {
    const eventSource = new EventSource('/api/events');
    eventSource.onmessage = (e) => {
        if (e.data === 'reset') {
            AppState.resetToSeedData();
            Router.navigate('/');
        }
    };
    eventSource.onerror = () => {
        // Silently reconnect
    };
}

// ---- Application initialization ----
function initApp() {
    // Initial state push to server
    AppState._persist();

    // Set up SSE
    initSSE();

    // Handle browser back/forward
    window.addEventListener('popstate', (e) => {
        const hash = window.location.hash.slice(1) || '/';
        Router.navigate(hash, true);
    });

    // Initial route
    const hash = window.location.hash.slice(1) || '/';
    Router.navigate(hash);
}

document.addEventListener('DOMContentLoaded', initApp);
