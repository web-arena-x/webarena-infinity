// ============================================================
// views.js — All view renderers and modal/action helpers
// ============================================================

const Views = {

    // ---- Home / Dashboard ----
    home() {
        const metrics = AppState.getAggregateMetrics('last_30_days', 'all');
        const lcpRating = AppState.getRating('lcp', metrics.lcp);
        const inpRating = AppState.getRating('inp', metrics.inp);
        const clsRating = AppState.getRating('cls', metrics.cls);
        const activeTheme = AppState.getActiveTheme();
        const installedApps = AppState.getInstalledApps();
        const pendingOpts = AppState.optimizations.filter(o => o.status === 'pending' || o.status === 'in_progress');
        const activeAlerts = AppState.alertRules.filter(a => a.enabled);

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">Web Performance Dashboard</h1>
                    <p class="page-subtitle">${Components.escapeHtml(AppState.store.name)} — ${Components.escapeHtml(AppState.store.url)}</p>
                </div>
            </div>

            ${Components.infoBox('Your performance scores are based on real user data from the past 30 days. <a href="#/reports">View detailed reports</a>')}

            <div class="grid grid-3 gap-md mt-md">
                ${Components.metricCard('lcp', metrics.lcp, lcpRating, { clickRoute: '/reports/over_time/lcp' })}
                ${Components.metricCard('inp', metrics.inp, inpRating, { clickRoute: '/reports/over_time/inp' })}
                ${Components.metricCard('cls', metrics.cls, clsRating, { clickRoute: '/reports/over_time/cls' })}
            </div>

            <div class="grid grid-2 gap-md mt-lg">
                <div class="card">
                    <div class="card-header">
                        <h3>Active Theme</h3>
                    </div>
                    <div class="card-body">
                        ${activeTheme ? `
                            <div class="flex flex-between">
                                <div>
                                    <strong>${Components.escapeHtml(activeTheme.name)}</strong>
                                    <span class="text-muted">v${activeTheme.version}</span>
                                    <div class="text-small text-muted mt-sm">by ${Components.escapeHtml(activeTheme.author)}</div>
                                </div>
                                <div class="text-right">
                                    <div class="metric-value">${activeTheme.performanceScore}</div>
                                    <div class="text-small text-muted">Performance Score</div>
                                </div>
                            </div>
                            <div class="mt-sm">
                                <a href="#/themes/${activeTheme.id}" data-route="/themes/${activeTheme.id}" class="btn btn-sm btn-secondary">Manage Theme</a>
                            </div>
                        ` : '<p class="text-muted">No active theme</p>'}
                    </div>
                </div>

                <div class="card">
                    <div class="card-header flex flex-between">
                        <h3>Installed Apps</h3>
                        <span class="badge badge-default">${installedApps.length} apps</span>
                    </div>
                    <div class="card-body">
                        <div class="text-small">
                            Total estimated impact: <strong class="rating-poor">+${installedApps.reduce((s, a) => s + a.performanceImpact.lcp, 0)}ms LCP</strong>
                        </div>
                        <div class="mt-sm">
                            <a href="#/apps" data-route="/apps" class="btn btn-sm btn-secondary">Manage Apps</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="grid grid-2 gap-md mt-md">
                <div class="card">
                    <div class="card-header flex flex-between">
                        <h3>Pending Optimizations</h3>
                        <span class="badge badge-warning">${pendingOpts.length}</span>
                    </div>
                    <div class="card-body">
                        ${pendingOpts.slice(0, 3).map(o => `
                            <div class="list-item">
                                <div>${Components.escapeHtml(o.title)}</div>
                                <div>${Components.priorityBadge(o.priority)}</div>
                            </div>
                        `).join('')}
                        ${pendingOpts.length > 3 ? `<div class="text-small text-muted mt-sm">+${pendingOpts.length - 3} more</div>` : ''}
                        <div class="mt-sm">
                            <a href="#/optimizations" data-route="/optimizations" class="btn btn-sm btn-secondary">View All</a>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header flex flex-between">
                        <h3>Active Alerts</h3>
                        <span class="badge badge-info">${activeAlerts.length}</span>
                    </div>
                    <div class="card-body">
                        ${activeAlerts.slice(0, 3).map(a => `
                            <div class="list-item">
                                <div>${Components.escapeHtml(a.name)}</div>
                                <div class="text-small text-muted">${a.metric.toUpperCase()} &gt; ${a.threshold}${a.metric === 'cls' ? '' : 'ms'}</div>
                            </div>
                        `).join('')}
                        <div class="mt-sm">
                            <a href="#/alerts" data-route="/alerts" class="btn btn-sm btn-secondary">Manage Alerts</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-header flex flex-between">
                    <h3>Recent Events</h3>
                    <a href="#/events" data-route="/events" class="btn btn-sm btn-secondary">View All</a>
                </div>
                <div class="card-body">
                    ${Components.eventTimeline(AppState.events.slice(-4))}
                </div>
            </div>
        `;
    },

    // ---- Themes ----
    themes() {
        const metrics = AppState.getAggregateMetrics('last_30_days', 'all');
        const lcpRating = AppState.getRating('lcp', metrics.lcp);
        const inpRating = AppState.getRating('inp', metrics.inp);
        const clsRating = AppState.getRating('cls', metrics.cls);
        const themes = AppState.themes;

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">Themes</h1>
                    <p class="page-subtitle">Manage your online store themes and view performance metrics</p>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-header">
                    <h3>Performance Metric Summary</h3>
                    <p class="text-small text-muted">Based on real user data from the past 30 days</p>
                </div>
                <div class="card-body">
                    <div class="grid grid-3 gap-md">
                        ${Components.metricCard('lcp', metrics.lcp, lcpRating, { clickRoute: '/reports/over_time/lcp' })}
                        ${Components.metricCard('inp', metrics.inp, inpRating, { clickRoute: '/reports/over_time/inp' })}
                        ${Components.metricCard('cls', metrics.cls, clsRating, { clickRoute: '/reports/over_time/cls' })}
                    </div>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-header flex flex-between">
                    <h3>Installed Themes</h3>
                </div>
                <div class="card-body">
                    ${themes.map(theme => `
                        <div class="theme-item" data-testid="theme-item-${theme.id}">
                            <div class="theme-info">
                                <div class="theme-name">
                                    <strong>${Components.escapeHtml(theme.name)}</strong>
                                    <span class="text-muted">v${theme.version}</span>
                                    ${theme.active ? '<span class="badge badge-good">Active</span>' : ''}
                                    ${theme.os2Compatible ? '<span class="badge badge-info">OS 2.0</span>' : '<span class="badge badge-warning">Legacy</span>'}
                                </div>
                                <div class="text-small text-muted">by ${Components.escapeHtml(theme.author)} &middot; ${theme.family} family</div>
                            </div>
                            <div class="theme-score">
                                <span class="metric-value ${theme.performanceScore >= 90 ? 'rating-good' : theme.performanceScore >= 75 ? 'rating-moderate' : 'rating-poor'}">${theme.performanceScore}</span>
                                <span class="text-small text-muted">score</span>
                            </div>
                            <div class="theme-actions">
                                ${!theme.active ? `<button class="btn btn-sm btn-primary" data-testid="activate-theme-${theme.id}" data-action="activate-theme" data-theme-id="${theme.id}">Activate</button>` : ''}
                                <a href="#/themes/${theme.id}" data-route="/themes/${theme.id}" class="btn btn-sm btn-secondary">Settings</a>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    },

    // ---- Theme Detail ----
    themeDetail(id) {
        const theme = AppState.getThemeById(id);
        if (!theme) return this._notFound('Theme not found');
        const tab = AppState.routeParams.tab || 'settings';

        const tabItems = [
            { id: 'settings', label: 'Settings' },
            { id: 'performance', label: 'Performance' }
        ];

        let content = '';
        if (tab === 'settings') {
            content = `
                <div class="card mt-md">
                    <div class="card-header"><h3>Theme Settings</h3></div>
                    <div class="card-body">
                        ${Components.formField('themeName', 'Theme Name', Components.textInput('themeName', theme.name, { disabled: true }))}
                        ${Components.formField('themeVersion', 'Version', Components.textInput('themeVersion', theme.version, { disabled: true }))}

                        <h4 class="mt-md mb-sm">Performance Settings</h4>
                        ${Components.toggleSwitch('pageTransitions', 'Enable page transitions', theme.settings.pageTransitions)}
                        ${Components.toggleSwitch('lazyLoading', 'Enable lazy loading', theme.settings.lazyLoading)}
                        ${Components.toggleSwitch('stickyHeader', 'Sticky header', theme.settings.stickyHeader)}
                        ${Components.toggleSwitch('predictiveSearch', 'Predictive search', theme.settings.predictiveSearch)}
                        ${Components.toggleSwitch('animationsEnabled', 'Enable animations', theme.settings.animationsEnabled)}

                        ${Components.formField('cartType', 'Cart type',
                            Components.dropdown('cartTypeDropdown', [
                                { value: 'drawer', label: 'Drawer' },
                                { value: 'page', label: 'Page' },
                                { value: 'popup', label: 'Popup' }
                            ], theme.settings.cartType)
                        )}

                        ${Components.formField('paginationLimit', 'Products per page',
                            Components.numberInput('paginationLimit', theme.settings.paginationLimit, { min: 4, max: 50 })
                        )}

                        <div class="mt-lg">
                            <button class="btn btn-primary" id="saveThemeSettingsBtn" data-testid="save-theme-settings">Save settings</button>
                        </div>
                    </div>
                </div>
            `;
        } else if (tab === 'performance') {
            content = `
                <div class="card mt-md">
                    <div class="card-header"><h3>Theme Performance</h3></div>
                    <div class="card-body">
                        <div class="flex flex-between">
                            <div>
                                <div class="text-small text-muted">Performance Score</div>
                                <div class="metric-value ${theme.performanceScore >= 90 ? 'rating-good' : theme.performanceScore >= 75 ? 'rating-moderate' : 'rating-poor'}">${theme.performanceScore}</div>
                            </div>
                            <div>
                                <div class="text-small text-muted">Family</div>
                                <div><strong>${theme.family}</strong></div>
                            </div>
                            <div>
                                <div class="text-small text-muted">OS 2.0 Compatible</div>
                                <div><strong>${theme.os2Compatible ? 'Yes' : 'No'}</strong></div>
                            </div>
                        </div>

                        ${theme.settings.pageTransitions || theme.settings.animationsEnabled ? Components.warningBox('Page transitions and animations are enabled. These can slow down your store. Consider disabling them for better performance.') : Components.successBox('No performance-impacting animations are enabled.')}
                        ${!theme.settings.lazyLoading ? Components.warningBox('Lazy loading is disabled. Enabling it can significantly improve loading speed.') : ''}
                    </div>
                </div>
            `;
        }

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">${Components.escapeHtml(theme.name)}</h1>
                    <p class="page-subtitle">v${theme.version} by ${Components.escapeHtml(theme.author)} ${theme.active ? '(Active)' : ''}</p>
                </div>
                <div class="page-actions">
                    ${!theme.active ? `<button class="btn btn-primary" data-testid="activate-theme-${theme.id}" data-action="activate-theme" data-theme-id="${theme.id}">Activate Theme</button>` : ''}
                </div>
            </div>
            ${Components.tabs('themeDetailTabs', tabItems, tab)}
            ${content}
        `;
    },

    // ---- Apps ----
    apps() {
        const installed = AppState.getInstalledApps();
        const available = AppState.getAvailableApps();

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">Apps</h1>
                    <p class="page-subtitle">Manage installed apps and their performance impact</p>
                </div>
            </div>

            ${Components.warningBox('Apps can significantly impact your store performance. Review each app\'s performance impact and remove apps that aren\'t providing enough value.')}

            <div class="card mt-md">
                <div class="card-header flex flex-between">
                    <h3>Installed Apps (${installed.length})</h3>
                    <div class="text-small">Total LCP impact: <strong class="rating-poor">+${installed.reduce((s, a) => s + a.performanceImpact.lcp, 0)}ms</strong></div>
                </div>
                <div class="card-body">
                    ${installed.map(app => `
                        <div class="app-card" data-testid="app-card-${app.id}">
                            <div class="app-icon" style="background-color: ${this._appColor(app.category)}">${app.name.charAt(0)}</div>
                            <div class="app-info">
                                <div class="app-name"><strong>${Components.escapeHtml(app.name)}</strong></div>
                                <div class="text-small text-muted">${Components.escapeHtml(app.developer)} &middot; ${Components.escapeHtml(app.category)}</div>
                                <div class="text-small text-muted">${Components.escapeHtml(app.description)}</div>
                            </div>
                            <div class="app-impact">
                                <div class="text-small">LCP: <span class="rating-poor">+${app.performanceImpact.lcp}ms</span></div>
                                <div class="text-small">INP: <span class="rating-poor">+${app.performanceImpact.inp}ms</span></div>
                                <div class="text-small">CLS: <span class="${app.performanceImpact.cls > 0.05 ? 'rating-poor' : 'rating-moderate'}">+${app.performanceImpact.cls.toFixed(2)}</span></div>
                            </div>
                            <div class="app-actions">
                                <a href="#/apps/${app.id}" data-route="/apps/${app.id}" class="btn btn-sm btn-secondary">Settings</a>
                                <button class="btn btn-sm btn-danger" data-testid="uninstall-app-${app.id}" data-action="uninstall-app" data-app-id="${app.id}">Uninstall</button>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>

            ${available.length > 0 ? `
                <div class="card mt-md">
                    <div class="card-header"><h3>Available Apps</h3></div>
                    <div class="card-body">
                        ${available.map(app => `
                            <div class="app-card" data-testid="app-card-${app.id}">
                                <div class="app-icon" style="background-color: ${this._appColor(app.category)}">${app.name.charAt(0)}</div>
                                <div class="app-info">
                                    <div class="app-name"><strong>${Components.escapeHtml(app.name)}</strong></div>
                                    <div class="text-small text-muted">${Components.escapeHtml(app.developer)} &middot; ${Components.escapeHtml(app.category)}</div>
                                    <div class="text-small text-muted">${Components.escapeHtml(app.description)}</div>
                                </div>
                                <div class="app-impact">
                                    <div class="text-small">Est. LCP: <span class="rating-moderate">+${app.performanceImpact.lcp}ms</span></div>
                                </div>
                                <div class="app-actions">
                                    <button class="btn btn-sm btn-primary" data-testid="install-app-${app.id}" data-action="install-app" data-app-id="${app.id}">Install</button>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
        `;
    },

    // ---- App Detail ----
    appDetail(id) {
        const app = AppState.getAppById(id);
        if (!app) return this._notFound('App not found');

        // Build settings form dynamically from app.settings
        let settingsHtml = '';
        for (const [key, value] of Object.entries(app.settings)) {
            const label = key.replace(/([A-Z])/g, ' $1').replace(/^./, s => s.toUpperCase());
            if (typeof value === 'boolean') {
                settingsHtml += Components.toggleSwitch(`appSetting_${key}`, label, value);
            } else if (typeof value === 'number') {
                settingsHtml += Components.formField(`appSetting_${key}`, label, Components.numberInput(`appSetting_${key}`, value));
            } else {
                settingsHtml += Components.formField(`appSetting_${key}`, label, Components.textInput(`appSetting_${key}`, value));
            }
        }

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">${Components.escapeHtml(app.name)}</h1>
                    <p class="page-subtitle">${Components.escapeHtml(app.developer)} &middot; ${Components.escapeHtml(app.category)}</p>
                </div>
                <div class="page-actions">
                    ${app.installed ? `<button class="btn btn-danger" data-testid="uninstall-app-${app.id}" data-action="uninstall-app" data-app-id="${app.id}">Uninstall</button>` :
                    `<button class="btn btn-primary" data-testid="install-app-${app.id}" data-action="install-app" data-app-id="${app.id}">Install</button>`}
                </div>
            </div>

            <div class="grid grid-2 gap-md mt-md">
                <div class="card">
                    <div class="card-header"><h3>Performance Impact</h3></div>
                    <div class="card-body">
                        <div class="list-item">
                            <span>LCP Impact</span>
                            <span class="rating-poor">+${app.performanceImpact.lcp}ms</span>
                        </div>
                        <div class="list-item">
                            <span>INP Impact</span>
                            <span class="rating-poor">+${app.performanceImpact.inp}ms</span>
                        </div>
                        <div class="list-item">
                            <span>CLS Impact</span>
                            <span class="${app.performanceImpact.cls > 0.05 ? 'rating-poor' : 'rating-moderate'}">+${app.performanceImpact.cls.toFixed(2)}</span>
                        </div>
                        <div class="list-item">
                            <span>Script Load Time</span>
                            <span>${app.scriptLoadTime}ms</span>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header"><h3>App Info</h3></div>
                    <div class="card-body">
                        <div class="list-item"><span>Status</span>${Components.statusBadge(app.status)}</div>
                        <div class="list-item"><span>Category</span><span>${Components.escapeHtml(app.category)}</span></div>
                        ${app.installedAt ? `<div class="list-item"><span>Installed</span><span>${Components.formatDate(app.installedAt)}</span></div>` : ''}
                        <div class="list-item"><span>Description</span><span class="text-small">${Components.escapeHtml(app.description)}</span></div>
                    </div>
                </div>
            </div>

            ${app.installed ? `
                <div class="card mt-md">
                    <div class="card-header"><h3>App Settings</h3></div>
                    <div class="card-body">
                        ${settingsHtml}
                        <div class="mt-lg">
                            <button class="btn btn-primary" id="saveAppSettingsBtn" data-testid="save-app-settings">Save settings</button>
                        </div>
                    </div>
                </div>
            ` : ''}
        `;
    },

    // ---- Reports ----
    reports() {
        const savedReports = AppState.savedReports;

        const builtInReports = [
            { metric: 'lcp', type: 'over_time', name: 'Largest Contentful Paint: Over Time' },
            { metric: 'inp', type: 'over_time', name: 'Interaction to Next Paint: Over Time' },
            { metric: 'cls', type: 'over_time', name: 'Cumulative Layout Shift: Over Time' },
            { metric: 'lcp', type: 'by_page_url', name: 'Largest Contentful Paint: Page URL' },
            { metric: 'inp', type: 'by_page_url', name: 'Interaction to Next Paint: Page URL' },
            { metric: 'cls', type: 'by_page_url', name: 'Cumulative Layout Shift: Page URL' },
            { metric: 'lcp', type: 'by_page_type', name: 'Largest Contentful Paint: Page Type' },
            { metric: 'inp', type: 'by_page_type', name: 'Interaction to Next Paint: Page Type' },
            { metric: 'cls', type: 'by_page_type', name: 'Cumulative Layout Shift: Page Type' }
        ];

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">Reports</h1>
                    <p class="page-subtitle">Web performance reports for your online store</p>
                </div>
                <div class="page-actions">
                    <button class="btn btn-primary" id="createReportBtn" data-testid="create-report-btn">Save Custom Report</button>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-header"><h3>Web Performance Reports</h3></div>
                <div class="card-body">
                    ${builtInReports.map(r => `
                        <div class="list-item clickable" data-route="/reports/${r.type}/${r.metric}" data-testid="report-link-${r.type}-${r.metric}">
                            <span>${Components.escapeHtml(r.name)}</span>
                            <span class="text-muted">&rarr;</span>
                        </div>
                    `).join('')}
                </div>
            </div>

            ${savedReports.length > 0 ? `
                <div class="card mt-md">
                    <div class="card-header flex flex-between">
                        <h3>Saved Reports</h3>
                    </div>
                    <div class="card-body">
                        ${savedReports.map(r => `
                            <div class="list-item" data-testid="saved-report-${r.id}">
                                <div data-route="/reports/${r.reportType}/${r.metric}" class="clickable">
                                    <strong>${Components.escapeHtml(r.name)}</strong>
                                    <div class="text-small text-muted">${r.metric.toUpperCase()} &middot; ${r.reportType.replace(/_/g, ' ')} &middot; ${r.filters.deviceType} &middot; ${r.filters.dateRange.replace(/_/g, ' ')}</div>
                                </div>
                                <button class="btn btn-sm btn-danger" data-testid="delete-report-${r.id}" data-action="delete-report" data-report-id="${r.id}">Delete</button>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
        `;
    },

    // ---- Report Detail ----
    reportDetail(type, metric) {
        const metricInfo = METRICS[metric.toUpperCase()];
        if (!metricInfo) return this._notFound('Metric not found');

        const dateRange = AppState.routeParams.dateRange || 'last_30_days';
        const deviceType = AppState.routeParams.deviceType || 'all';

        const typeLabels = { over_time: 'Over Time', by_page_url: 'Page URL', by_page_type: 'Page Type' };
        const title = `${metricInfo.name}: ${typeLabels[type] || type}`;

        let contentHtml = '';

        if (type === 'over_time') {
            const data = AppState.getPerformanceOverTime(metric, dateRange, deviceType);
            const chartData = data.map(d => ({
                value: d.value,
                label: Components.formatDateShort(d.date)
            }));
            const maxVal = Math.max(...data.map(d => d.value || 0), 1);

            contentHtml = `
                ${Components.barChart('perfChart', chartData, { metric, maxValue: maxVal * 1.2, height: 250 })}

                <div class="mt-lg">
                    ${Components.dataTable('perfTable', [
                        { key: 'date', label: 'Date', render: r => Components.formatDate(r.date) },
                        { key: 'value', label: `${metricInfo.shortName} P75`, align: 'right', render: r => `<span class="${Components.getRatingClass(AppState.getRating(metric, r.value))}">${Components.formatMetricValue(metric, r.value)}${Components.formatMetricUnit(metric)}</span>` },
                        { key: 'sessions', label: 'Sessions', align: 'right', render: r => r.sessions.toLocaleString() },
                        { key: 'distribution', label: 'Distribution', render: r => Components.distributionBar(r.good, r.moderate, r.poor) }
                    ], data)}
                </div>
            `;
        } else if (type === 'by_page_url') {
            const data = AppState.getPerformanceByPageUrl(dateRange, deviceType);
            contentHtml = Components.dataTable('perfTable', [
                { key: 'path', label: 'Page Path', render: r => `<a href="#/pages/${r.pageId}" data-route="/pages/${r.pageId}">${Components.escapeHtml(r.path)}</a>` },
                { key: 'name', label: 'Page Name', render: r => Components.escapeHtml(r.name) },
                { key: 'type', label: 'Type', render: r => `<span class="tag">${r.type}</span>` },
                { key: metric, label: `${metricInfo.shortName} P75`, align: 'right', render: r => `<span class="${Components.getRatingClass(AppState.getRating(metric, r[metric]))}">${Components.formatMetricValue(metric, r[metric])}${Components.formatMetricUnit(metric)}</span>` },
                { key: 'sessions', label: 'Sessions', align: 'right', render: r => r.sessions.toLocaleString() }
            ], data);
        } else if (type === 'by_page_type') {
            const data = AppState.getPerformanceByPageType(dateRange, deviceType);
            contentHtml = Components.dataTable('perfTable', [
                { key: 'pageType', label: 'Page Type', render: r => `<span class="tag">${r.pageType}</span>` },
                { key: metric, label: `${metricInfo.shortName} P75`, align: 'right', render: r => `<span class="${Components.getRatingClass(AppState.getRating(metric, r[metric]))}">${Components.formatMetricValue(metric, r[metric])}${Components.formatMetricUnit(metric)}</span>` },
                { key: 'sessions', label: 'Sessions', align: 'right', render: r => r.sessions.toLocaleString() }
            ], data);
        }

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">${Components.escapeHtml(title)}</h1>
                    <p class="page-subtitle">75th percentile measurement</p>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-header">
                    <div class="flex gap-md">
                        ${Components.dropdown('dateRangeFilter', [
                            { value: 'today', label: 'Today' },
                            { value: 'last_7_days', label: 'Last 7 days' },
                            { value: 'last_30_days', label: 'Last 30 days' }
                        ], dateRange, { placeholder: 'Date range' })}

                        ${Components.dropdown('deviceTypeFilter', [
                            { value: 'all', label: 'All devices' },
                            { value: 'desktop', label: 'Desktop' },
                            { value: 'mobile', label: 'Mobile' }
                        ], deviceType, { placeholder: 'Device type' })}
                    </div>
                </div>
                <div class="card-body">
                    ${contentHtml}
                </div>
            </div>
        `;
    },

    // ---- Pages ----
    pages() {
        const pages = AppState.pages;

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">Monitored Pages</h1>
                    <p class="page-subtitle">Pages being tracked for web performance metrics</p>
                </div>
                <div class="page-actions">
                    <button class="btn btn-primary" id="addPageBtn" data-testid="add-page-btn">Add Page</button>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-body">
                    ${Components.dataTable('pagesTable', [
                        { key: 'name', label: 'Page', render: r => `<a href="#/pages/${r.id}" data-route="/pages/${r.id}"><strong>${Components.escapeHtml(r.name)}</strong></a><div class="text-small text-muted">${Components.escapeHtml(r.path)}</div>` },
                        { key: 'type', label: 'Type', render: r => `<span class="tag">${r.type}</span>` },
                        { key: 'priority', label: 'Priority', render: r => Components.priorityBadge(r.priority) },
                        { key: 'monitored', label: 'Monitoring', render: r => `<span class="status-dot ${r.monitored ? 'status-active' : 'status-inactive'}"></span> ${r.monitored ? 'Active' : 'Paused'}` },
                        { key: 'actions', label: '', render: r => `
                            <button class="btn btn-sm btn-secondary" data-action="toggle-monitoring" data-page-id="${r.id}" data-testid="toggle-monitoring-${r.id}">${r.monitored ? 'Pause' : 'Resume'}</button>
                            <button class="btn btn-sm btn-danger" data-action="remove-page" data-page-id="${r.id}" data-testid="remove-page-${r.id}">Remove</button>
                        ` }
                    ], pages)}
                </div>
            </div>
        `;
    },

    // ---- Page Detail ----
    pageDetail(id) {
        const page = AppState.getPageById(id);
        if (!page) return this._notFound('Page not found');

        const records = AppState.getPerformanceForPage(page.id, 'last_30_days', 'all');
        function p75(arr) {
            if (!arr.length) return null;
            const sorted = [...arr].sort((a, b) => a - b);
            return sorted[Math.ceil(sorted.length * 0.75) - 1];
        }
        const lcp = p75(records.map(r => r.lcp));
        const inp = p75(records.map(r => r.inp));
        const cls = p75(records.map(r => r.cls));

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">${Components.escapeHtml(page.name)}</h1>
                    <p class="page-subtitle">${Components.escapeHtml(page.path)} &middot; ${page.type}</p>
                </div>
                <div class="page-actions">
                    <button class="btn btn-secondary" data-action="toggle-monitoring" data-page-id="${page.id}" data-testid="toggle-monitoring-${page.id}">${page.monitored ? 'Pause Monitoring' : 'Resume Monitoring'}</button>
                </div>
            </div>

            <div class="grid grid-3 gap-md mt-md">
                ${Components.metricCard('lcp', lcp, AppState.getRating('lcp', lcp))}
                ${Components.metricCard('inp', inp, AppState.getRating('inp', inp))}
                ${Components.metricCard('cls', cls, AppState.getRating('cls', cls))}
            </div>

            <div class="card mt-md">
                <div class="card-header"><h3>Page Settings</h3></div>
                <div class="card-body">
                    ${Components.formField('pageName', 'Page Name', Components.textInput('pageName', page.name))}
                    ${Components.formField('pagePath', 'Page Path', Components.textInput('pagePath', page.path))}
                    ${Components.formField('pageType', 'Page Type',
                        Components.dropdown('pageTypeDropdown', PAGE_TYPES.map(t => ({ value: t, label: t.charAt(0).toUpperCase() + t.slice(1) })), page.type)
                    )}
                    ${Components.formField('pagePriority', 'Priority',
                        Components.dropdown('pagePriorityDropdown', OPTIMIZATION_PRIORITIES.map(p => ({ value: p, label: p.charAt(0).toUpperCase() + p.slice(1) })), page.priority)
                    )}
                    <div class="mt-lg">
                        <button class="btn btn-primary" id="savePageSettingsBtn" data-testid="save-page-settings">Save settings</button>
                    </div>
                </div>
            </div>
        `;
    },

    // ---- Optimizations ----
    optimizations() {
        const opts = AppState.optimizations;
        const tab = AppState.routeParams.tab || 'active';

        const filtered = tab === 'active' ? opts.filter(o => o.status === 'pending' || o.status === 'in_progress') :
                          tab === 'completed' ? opts.filter(o => o.status === 'completed') :
                          tab === 'dismissed' ? opts.filter(o => o.status === 'dismissed') : opts;

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">Performance Optimizations</h1>
                    <p class="page-subtitle">Track and manage optimization actions for your store</p>
                </div>
                <div class="page-actions">
                    <button class="btn btn-primary" id="addOptimizationBtn" data-testid="add-optimization-btn">Add Optimization</button>
                </div>
            </div>

            ${Components.tabs('optimizationTabs', [
                { id: 'active', label: 'Active' },
                { id: 'completed', label: 'Completed' },
                { id: 'dismissed', label: 'Dismissed' },
                { id: 'all', label: 'All' }
            ], tab)}

            <div class="card mt-md">
                <div class="card-body">
                    ${filtered.length === 0 ? Components.emptyState('No optimizations in this category') : ''}
                    ${filtered.map(opt => `
                        <div class="optimization-item" data-testid="optimization-item-${opt.id}">
                            <div class="optimization-info">
                                <div class="flex gap-sm">
                                    ${Components.priorityBadge(opt.priority)}
                                    ${Components.statusBadge(opt.status)}
                                    <span class="tag">${opt.metric.toUpperCase()}</span>
                                    <span class="tag">${opt.category}</span>
                                </div>
                                <h4 class="mt-sm">${Components.escapeHtml(opt.title)}</h4>
                                <p class="text-small text-muted">${Components.escapeHtml(opt.description)}</p>
                                <div class="text-small mt-sm">
                                    <span class="text-muted">Estimated impact:</span> <strong>${Components.escapeHtml(opt.estimatedImpact)}</strong>
                                    &middot; <span class="text-muted">Affects:</span> ${Components.escapeHtml(opt.pageAffected)}
                                </div>
                            </div>
                            <div class="optimization-actions">
                                ${opt.status === 'pending' ? `
                                    <button class="btn btn-sm btn-primary" data-action="start-optimization" data-opt-id="${opt.id}" data-testid="start-opt-${opt.id}">Start</button>
                                    <button class="btn btn-sm btn-secondary" data-action="dismiss-optimization" data-opt-id="${opt.id}" data-testid="dismiss-opt-${opt.id}">Dismiss</button>
                                ` : ''}
                                ${opt.status === 'in_progress' ? `
                                    <button class="btn btn-sm btn-primary" data-action="complete-optimization" data-opt-id="${opt.id}" data-testid="complete-opt-${opt.id}">Complete</button>
                                ` : ''}
                                <button class="btn btn-sm btn-danger" data-action="remove-optimization" data-opt-id="${opt.id}" data-testid="remove-opt-${opt.id}">Remove</button>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    },

    // ---- Alerts ----
    alerts() {
        const rules = AppState.alertRules;

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">Alert Rules</h1>
                    <p class="page-subtitle">Get notified when performance metrics exceed thresholds</p>
                </div>
                <div class="page-actions">
                    <button class="btn btn-primary" id="addAlertBtn" data-testid="add-alert-btn">Add Alert Rule</button>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-body">
                    ${rules.length === 0 ? Components.emptyState('No alert rules configured') : ''}
                    ${rules.map(rule => `
                        <div class="alert-item" data-testid="alert-item-${rule.id}">
                            <div class="alert-info">
                                <div class="flex gap-sm">
                                    <span class="status-dot ${rule.enabled ? 'status-active' : 'status-inactive'}"></span>
                                    <strong>${Components.escapeHtml(rule.name)}</strong>
                                </div>
                                <div class="text-small text-muted mt-sm">
                                    ${rule.metric.toUpperCase()} ${rule.condition === 'greater_than' ? '>' : '<'} ${rule.threshold}${rule.metric === 'cls' ? '' : 'ms'}
                                    &middot; Pages: ${rule.pageType} &middot; Device: ${rule.deviceType}
                                    ${rule.notifyEmail ? ' &middot; Email notifications' : ''}
                                </div>
                            </div>
                            <div class="alert-actions">
                                <button class="btn btn-sm btn-secondary" data-action="toggle-alert" data-alert-id="${rule.id}" data-testid="toggle-alert-${rule.id}">${rule.enabled ? 'Disable' : 'Enable'}</button>
                                <button class="btn btn-sm btn-secondary" data-action="edit-alert" data-alert-id="${rule.id}" data-testid="edit-alert-${rule.id}">Edit</button>
                                <button class="btn btn-sm btn-danger" data-action="remove-alert" data-alert-id="${rule.id}" data-testid="remove-alert-${rule.id}">Remove</button>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    },

    // ---- Events ----
    events() {
        const events = AppState.events;

        return `
            <div class="page-header">
                <div>
                    <h1 class="page-title">Event Annotations</h1>
                    <p class="page-subtitle">Track changes that could impact your store's web performance</p>
                </div>
                <div class="page-actions">
                    <button class="btn btn-primary" id="addEventBtn" data-testid="add-event-btn">Add Event</button>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-body">
                    ${Components.eventTimeline(events)}
                </div>
            </div>
        `;
    },

    // ---- Settings ----
    settings() {
        const store = AppState.store;
        const budgets = AppState.performanceBudgets;

        return `
            <div class="page-header">
                <h1 class="page-title">Settings</h1>
            </div>

            <div class="card mt-md">
                <div class="card-header"><h3>Store Information</h3></div>
                <div class="card-body">
                    ${Components.formField('storeName', 'Store name', Components.textInput('storeName', store.name))}
                    ${Components.formField('storeUrl', 'Store URL', Components.textInput('storeUrl', store.url, { disabled: true }))}
                    ${Components.formField('storeDomain', 'Custom domain', Components.textInput('storeDomain', store.domain))}
                    ${Components.toggleSwitch('passwordProtected', 'Password protection', store.passwordProtected)}
                    ${store.passwordProtected ? Components.warningBox('Your store is password-protected. Real user metrics (Core Web Vitals) cannot be collected while password protection is enabled.') : ''}
                    <div class="mt-lg">
                        <button class="btn btn-primary" id="saveStoreSettingsBtn" data-testid="save-store-settings">Save settings</button>
                    </div>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-header"><h3>Performance Budgets</h3></div>
                <div class="card-body">
                    ${Components.infoBox('Performance budgets help you track when metrics exceed your target thresholds.')}

                    <h4 class="mt-md">LCP (Largest Contentful Paint)</h4>
                    <div class="grid grid-2 gap-md">
                        ${Components.formField('lcpTarget', 'Target (ms)', Components.numberInput('lcpTarget', budgets.lcp.target, { min: 0, step: 100 }))}
                        ${Components.formField('lcpWarning', 'Warning (ms)', Components.numberInput('lcpWarning', budgets.lcp.warning, { min: 0, step: 100 }))}
                    </div>

                    <h4 class="mt-md">INP (Interaction to Next Paint)</h4>
                    <div class="grid grid-2 gap-md">
                        ${Components.formField('inpTarget', 'Target (ms)', Components.numberInput('inpTarget', budgets.inp.target, { min: 0, step: 50 }))}
                        ${Components.formField('inpWarning', 'Warning (ms)', Components.numberInput('inpWarning', budgets.inp.warning, { min: 0, step: 50 }))}
                    </div>

                    <h4 class="mt-md">CLS (Cumulative Layout Shift)</h4>
                    <div class="grid grid-2 gap-md">
                        ${Components.formField('clsTarget', 'Target', Components.numberInput('clsTarget', budgets.cls.target, { min: 0, max: 1, step: 0.01 }))}
                        ${Components.formField('clsWarning', 'Warning', Components.numberInput('clsWarning', budgets.cls.warning, { min: 0, max: 1, step: 0.01 }))}
                    </div>

                    <div class="mt-lg">
                        <button class="btn btn-primary" id="saveBudgetsBtn" data-testid="save-budgets">Save budgets</button>
                    </div>
                </div>
            </div>

            <div class="card mt-md">
                <div class="card-header"><h3>Data Management</h3></div>
                <div class="card-body">
                    ${Components.warningBox('Resetting data will restore all settings, apps, themes, and reports to their default values.')}
                    <div class="mt-md">
                        <button class="btn btn-danger" id="resetDataBtn" data-testid="reset-data-btn">Reset all data to defaults</button>
                    </div>
                </div>
            </div>
        `;
    },

    // ---- Modal Helpers ----

    _showAddPageModal() {
        const body = `
            ${Components.formField('newPageName', 'Page name', Components.textInput('newPageName', '', { placeholder: 'e.g., Holiday Sale Page' }), { required: true })}
            ${Components.formField('newPagePath', 'Page path', Components.textInput('newPagePath', '', { placeholder: 'e.g., /collections/holiday-sale' }), { required: true })}
            ${Components.formField('newPageType', 'Page type',
                Components.dropdown('newPageTypeDropdown', PAGE_TYPES.map(t => ({ value: t, label: t.charAt(0).toUpperCase() + t.slice(1) })), 'page')
            )}
            ${Components.formField('newPagePriority', 'Priority',
                Components.dropdown('newPagePriorityDropdown', OPTIMIZATION_PRIORITIES.map(p => ({ value: p, label: p.charAt(0).toUpperCase() + p.slice(1) })), 'medium')
            )}
        `;
        const footer = `
            <button class="btn btn-secondary" data-testid="modal-cancel" onclick="Components.closeModal()">Cancel</button>
            <button class="btn btn-primary" data-testid="submit-add-page" id="submitAddPage">Add Page</button>
        `;
        Components.showModal('Add Page', body, footer);

        setTimeout(() => {
            const btn = document.getElementById('submitAddPage');
            if (btn) {
                btn.addEventListener('click', () => {
                    const name = document.getElementById('newPageName').value.trim();
                    const path = document.getElementById('newPagePath').value.trim();
                    const type = document.getElementById('newPageTypeDropdown').getAttribute('data-value') || 'page';
                    const priority = document.getElementById('newPagePriorityDropdown').getAttribute('data-value') || 'medium';

                    if (!name || !path) {
                        Components.showToast('Please fill in all required fields', 'error');
                        return;
                    }

                    AppState.addPage({ name, path, type, priority, monitored: true });
                    Components.closeModal();
                    Components.showToast('Page added successfully', 'success');
                    Router.refresh();
                });
            }
        }, 50);
    },

    _showAddEventModal() {
        const body = `
            ${Components.formField('newEventTitle', 'Title', Components.textInput('newEventTitle', '', { placeholder: 'e.g., Updated checkout flow' }), { required: true })}
            ${Components.formField('newEventDescription', 'Description', Components.textarea('newEventDescription', '', { placeholder: 'Describe the change...' }))}
            ${Components.formField('newEventDate', 'Date', Components.dateInput('newEventDate', new Date().toISOString().split('T')[0]), { required: true })}
            ${Components.formField('newEventType', 'Event type',
                Components.dropdown('newEventTypeDropdown', [
                    { value: 'app_installed', label: 'App Installed' },
                    { value: 'app_uninstalled', label: 'App Uninstalled' },
                    { value: 'theme_changed', label: 'Theme Changed' },
                    { value: 'theme_updated', label: 'Theme Updated' },
                    { value: 'code_change', label: 'Code Change' },
                    { value: 'custom', label: 'Custom' }
                ], 'custom')
            )}
            ${Components.formField('newEventMetric', 'Affected metric',
                Components.dropdown('newEventMetricDropdown', [
                    { value: 'all', label: 'All Metrics' },
                    { value: 'lcp', label: 'LCP' },
                    { value: 'inp', label: 'INP' },
                    { value: 'cls', label: 'CLS' }
                ], 'all')
            )}
            ${Components.formField('newEventImpact', 'Expected impact',
                Components.dropdown('newEventImpactDropdown', [
                    { value: 'positive', label: 'Positive' },
                    { value: 'negative', label: 'Negative' },
                    { value: 'neutral', label: 'Neutral' }
                ], 'neutral')
            )}
        `;
        const footer = `
            <button class="btn btn-secondary" data-testid="modal-cancel" onclick="Components.closeModal()">Cancel</button>
            <button class="btn btn-primary" data-testid="submit-add-event" id="submitAddEvent">Add Event</button>
        `;
        Components.showModal('Add Event Annotation', body, footer);

        setTimeout(() => {
            const btn = document.getElementById('submitAddEvent');
            if (btn) {
                btn.addEventListener('click', () => {
                    const title = document.getElementById('newEventTitle').value.trim();
                    const description = document.getElementById('newEventDescription').value.trim();
                    const date = document.getElementById('newEventDate').value.trim();
                    const type = document.getElementById('newEventTypeDropdown').getAttribute('data-value') || 'custom';
                    const metric = document.getElementById('newEventMetricDropdown').getAttribute('data-value') || 'all';
                    const impact = document.getElementById('newEventImpactDropdown').getAttribute('data-value') || 'neutral';

                    if (!title) {
                        Components.showToast('Please enter an event title', 'error');
                        return;
                    }

                    AppState.addEvent({ title, description, date: date + 'T00:00:00Z', type, metric, impact });
                    Components.closeModal();
                    Components.showToast('Event added successfully', 'success');
                    Router.refresh();
                });
            }
        }, 50);
    },

    _showEditEventModal(eventId) {
        const event = AppState.getEventById(eventId);
        if (!event) return;

        const body = `
            ${Components.formField('editEventTitle', 'Title', Components.textInput('editEventTitle', event.title), { required: true })}
            ${Components.formField('editEventDescription', 'Description', Components.textarea('editEventDescription', event.description))}
            ${Components.formField('editEventDate', 'Date', Components.dateInput('editEventDate', event.date.split('T')[0]), { required: true })}
            ${Components.formField('editEventType', 'Event type',
                Components.dropdown('editEventTypeDropdown', [
                    { value: 'app_installed', label: 'App Installed' },
                    { value: 'app_uninstalled', label: 'App Uninstalled' },
                    { value: 'theme_changed', label: 'Theme Changed' },
                    { value: 'theme_updated', label: 'Theme Updated' },
                    { value: 'code_change', label: 'Code Change' },
                    { value: 'custom', label: 'Custom' }
                ], event.type)
            )}
            ${Components.formField('editEventMetric', 'Affected metric',
                Components.dropdown('editEventMetricDropdown', [
                    { value: 'all', label: 'All Metrics' },
                    { value: 'lcp', label: 'LCP' },
                    { value: 'inp', label: 'INP' },
                    { value: 'cls', label: 'CLS' }
                ], event.metric)
            )}
            ${Components.formField('editEventImpact', 'Expected impact',
                Components.dropdown('editEventImpactDropdown', [
                    { value: 'positive', label: 'Positive' },
                    { value: 'negative', label: 'Negative' },
                    { value: 'neutral', label: 'Neutral' }
                ], event.impact)
            )}
        `;
        const footer = `
            <button class="btn btn-secondary" data-testid="modal-cancel" onclick="Components.closeModal()">Cancel</button>
            <button class="btn btn-primary" data-testid="submit-edit-event" id="submitEditEvent">Save Changes</button>
        `;
        Components.showModal('Edit Event', body, footer);

        setTimeout(() => {
            const btn = document.getElementById('submitEditEvent');
            if (btn) {
                btn.addEventListener('click', () => {
                    const title = document.getElementById('editEventTitle').value.trim();
                    const description = document.getElementById('editEventDescription').value.trim();
                    const date = document.getElementById('editEventDate').value.trim();
                    const type = document.getElementById('editEventTypeDropdown').getAttribute('data-value');
                    const metric = document.getElementById('editEventMetricDropdown').getAttribute('data-value');
                    const impact = document.getElementById('editEventImpactDropdown').getAttribute('data-value');

                    if (!title) {
                        Components.showToast('Please enter an event title', 'error');
                        return;
                    }

                    AppState.updateEvent(eventId, { title, description, date: date + 'T00:00:00Z', type, metric, impact });
                    Components.closeModal();
                    Components.showToast('Event updated successfully', 'success');
                    Router.refresh();
                });
            }
        }, 50);
    },

    _showAddAlertModal() {
        const body = `
            ${Components.formField('newAlertName', 'Alert name', Components.textInput('newAlertName', '', { placeholder: 'e.g., Mobile LCP Alert' }), { required: true })}
            ${Components.formField('newAlertMetric', 'Metric',
                Components.dropdown('newAlertMetricDropdown', [
                    { value: 'lcp', label: 'LCP (Largest Contentful Paint)' },
                    { value: 'inp', label: 'INP (Interaction to Next Paint)' },
                    { value: 'cls', label: 'CLS (Cumulative Layout Shift)' }
                ], 'lcp'), { required: true }
            )}
            ${Components.formField('newAlertCondition', 'Condition',
                Components.dropdown('newAlertConditionDropdown', [
                    { value: 'greater_than', label: 'Greater than' },
                    { value: 'less_than', label: 'Less than' }
                ], 'greater_than')
            )}
            ${Components.formField('newAlertThreshold', 'Threshold', Components.numberInput('newAlertThreshold', 2500, { min: 0, step: 100 }), { required: true })}
            ${Components.formField('newAlertPageType', 'Page type',
                Components.dropdown('newAlertPageTypeDropdown', [
                    { value: 'all', label: 'All page types' },
                    ...PAGE_TYPES.map(t => ({ value: t, label: t.charAt(0).toUpperCase() + t.slice(1) }))
                ], 'all')
            )}
            ${Components.formField('newAlertDeviceType', 'Device type',
                Components.dropdown('newAlertDeviceTypeDropdown', [
                    { value: 'all', label: 'All devices' },
                    { value: 'desktop', label: 'Desktop' },
                    { value: 'mobile', label: 'Mobile' }
                ], 'all')
            )}
            ${Components.checkbox('newAlertEnabled', 'Enabled', true)}
            ${Components.checkbox('newAlertNotifyEmail', 'Send email notifications', true)}
        `;
        const footer = `
            <button class="btn btn-secondary" data-testid="modal-cancel" onclick="Components.closeModal()">Cancel</button>
            <button class="btn btn-primary" data-testid="submit-add-alert" id="submitAddAlert">Add Alert</button>
        `;
        Components.showModal('Add Alert Rule', body, footer);

        setTimeout(() => {
            document.getElementById('submitAddAlert').addEventListener('click', () => {
                const name = document.getElementById('newAlertName').value.trim();
                const metric = document.getElementById('newAlertMetricDropdown').getAttribute('data-value') || 'lcp';
                const condition = document.getElementById('newAlertConditionDropdown').getAttribute('data-value') || 'greater_than';
                const threshold = parseFloat(document.getElementById('newAlertThreshold').value);
                const pageType = document.getElementById('newAlertPageTypeDropdown').getAttribute('data-value') || 'all';
                const deviceType = document.getElementById('newAlertDeviceTypeDropdown').getAttribute('data-value') || 'all';
                const enabled = document.getElementById('newAlertEnabled').checked;
                const notifyEmail = document.getElementById('newAlertNotifyEmail').checked;

                if (!name || isNaN(threshold)) {
                    Components.showToast('Please fill in all required fields', 'error');
                    return;
                }

                AppState.addAlertRule({ name, metric, condition, threshold, pageType, deviceType, enabled, notifyEmail });
                Components.closeModal();
                Components.showToast('Alert rule created', 'success');
                Router.refresh();
            });
        }, 50);
    },

    _showEditAlertModal(alertId) {
        const rule = AppState.getAlertById(alertId);
        if (!rule) return;

        const body = `
            ${Components.formField('editAlertName', 'Alert name', Components.textInput('editAlertName', rule.name), { required: true })}
            ${Components.formField('editAlertMetric', 'Metric',
                Components.dropdown('editAlertMetricDropdown', [
                    { value: 'lcp', label: 'LCP (Largest Contentful Paint)' },
                    { value: 'inp', label: 'INP (Interaction to Next Paint)' },
                    { value: 'cls', label: 'CLS (Cumulative Layout Shift)' }
                ], rule.metric), { required: true }
            )}
            ${Components.formField('editAlertCondition', 'Condition',
                Components.dropdown('editAlertConditionDropdown', [
                    { value: 'greater_than', label: 'Greater than' },
                    { value: 'less_than', label: 'Less than' }
                ], rule.condition)
            )}
            ${Components.formField('editAlertThreshold', 'Threshold', Components.numberInput('editAlertThreshold', rule.threshold, { min: 0, step: 100 }), { required: true })}
            ${Components.formField('editAlertPageType', 'Page type',
                Components.dropdown('editAlertPageTypeDropdown', [
                    { value: 'all', label: 'All page types' },
                    ...PAGE_TYPES.map(t => ({ value: t, label: t.charAt(0).toUpperCase() + t.slice(1) }))
                ], rule.pageType)
            )}
            ${Components.formField('editAlertDeviceType', 'Device type',
                Components.dropdown('editAlertDeviceTypeDropdown', [
                    { value: 'all', label: 'All devices' },
                    { value: 'desktop', label: 'Desktop' },
                    { value: 'mobile', label: 'Mobile' }
                ], rule.deviceType)
            )}
            ${Components.checkbox('editAlertEnabled', 'Enabled', rule.enabled)}
            ${Components.checkbox('editAlertNotifyEmail', 'Send email notifications', rule.notifyEmail)}
        `;
        const footer = `
            <button class="btn btn-secondary" data-testid="modal-cancel" onclick="Components.closeModal()">Cancel</button>
            <button class="btn btn-primary" data-testid="submit-edit-alert" id="submitEditAlert">Save Changes</button>
        `;
        Components.showModal('Edit Alert Rule', body, footer);

        setTimeout(() => {
            document.getElementById('submitEditAlert').addEventListener('click', () => {
                const name = document.getElementById('editAlertName').value.trim();
                const metric = document.getElementById('editAlertMetricDropdown').getAttribute('data-value');
                const condition = document.getElementById('editAlertConditionDropdown').getAttribute('data-value');
                const threshold = parseFloat(document.getElementById('editAlertThreshold').value);
                const pageType = document.getElementById('editAlertPageTypeDropdown').getAttribute('data-value');
                const deviceType = document.getElementById('editAlertDeviceTypeDropdown').getAttribute('data-value');
                const enabled = document.getElementById('editAlertEnabled').checked;
                const notifyEmail = document.getElementById('editAlertNotifyEmail').checked;

                if (!name || isNaN(threshold)) {
                    Components.showToast('Please fill in required fields', 'error');
                    return;
                }

                AppState.updateAlertRule(alertId, { name, metric, condition, threshold, pageType, deviceType, enabled, notifyEmail });
                Components.closeModal();
                Components.showToast('Alert rule updated', 'success');
                Router.refresh();
            });
        }, 50);
    },

    _showAddOptimizationModal() {
        const body = `
            ${Components.formField('newOptTitle', 'Title', Components.textInput('newOptTitle', '', { placeholder: 'e.g., Optimize product images' }), { required: true })}
            ${Components.formField('newOptDescription', 'Description', Components.textarea('newOptDescription', '', { placeholder: 'Describe the optimization...' }))}
            ${Components.formField('newOptMetric', 'Target metric',
                Components.dropdown('newOptMetricDropdown', [
                    { value: 'lcp', label: 'LCP' },
                    { value: 'inp', label: 'INP' },
                    { value: 'cls', label: 'CLS' }
                ], 'lcp'), { required: true }
            )}
            ${Components.formField('newOptPriority', 'Priority',
                Components.dropdown('newOptPriorityDropdown', OPTIMIZATION_PRIORITIES.map(p => ({ value: p, label: p.charAt(0).toUpperCase() + p.slice(1) })), 'medium')
            )}
            ${Components.formField('newOptCategory', 'Category',
                Components.dropdown('newOptCategoryDropdown', OPTIMIZATION_CATEGORIES.map(c => ({ value: c, label: c.charAt(0).toUpperCase() + c.slice(1) })), 'other')
            )}
            ${Components.formField('newOptImpact', 'Estimated impact', Components.textInput('newOptImpact', '', { placeholder: 'e.g., 200ms LCP improvement' }))}
            ${Components.formField('newOptPageAffected', 'Page affected', Components.textInput('newOptPageAffected', '*', { placeholder: 'e.g., /products/* or *' }))}
        `;
        const footer = `
            <button class="btn btn-secondary" data-testid="modal-cancel" onclick="Components.closeModal()">Cancel</button>
            <button class="btn btn-primary" data-testid="submit-add-optimization" id="submitAddOptimization">Add Optimization</button>
        `;
        Components.showModal('Add Optimization', body, footer);

        setTimeout(() => {
            document.getElementById('submitAddOptimization').addEventListener('click', () => {
                const title = document.getElementById('newOptTitle').value.trim();
                const description = document.getElementById('newOptDescription').value.trim();
                const metric = document.getElementById('newOptMetricDropdown').getAttribute('data-value') || 'lcp';
                const priority = document.getElementById('newOptPriorityDropdown').getAttribute('data-value') || 'medium';
                const category = document.getElementById('newOptCategoryDropdown').getAttribute('data-value') || 'other';
                const estimatedImpact = document.getElementById('newOptImpact').value.trim();
                const pageAffected = document.getElementById('newOptPageAffected').value.trim() || '*';

                if (!title) {
                    Components.showToast('Please enter a title', 'error');
                    return;
                }

                AppState.addOptimization({ title, description, metric, priority, category, estimatedImpact, pageAffected });
                Components.closeModal();
                Components.showToast('Optimization added', 'success');
                Router.refresh();
            });
        }, 50);
    },

    _showCreateReportModal() {
        const body = `
            ${Components.formField('newReportName', 'Report name', Components.textInput('newReportName', '', { placeholder: 'e.g., Weekly Mobile LCP' }), { required: true })}
            ${Components.formField('newReportMetric', 'Metric',
                Components.dropdown('newReportMetricDropdown', [
                    { value: 'lcp', label: 'LCP (Largest Contentful Paint)' },
                    { value: 'inp', label: 'INP (Interaction to Next Paint)' },
                    { value: 'cls', label: 'CLS (Cumulative Layout Shift)' }
                ], 'lcp'), { required: true }
            )}
            ${Components.formField('newReportType', 'Report type',
                Components.dropdown('newReportTypeDropdown', [
                    { value: 'over_time', label: 'Over Time' },
                    { value: 'by_page_url', label: 'By Page URL' },
                    { value: 'by_page_type', label: 'By Page Type' }
                ], 'over_time'), { required: true }
            )}
            ${Components.formField('newReportDeviceType', 'Device type',
                Components.dropdown('newReportDeviceTypeDropdown', [
                    { value: 'all', label: 'All devices' },
                    { value: 'desktop', label: 'Desktop' },
                    { value: 'mobile', label: 'Mobile' }
                ], 'all')
            )}
            ${Components.formField('newReportDateRange', 'Date range',
                Components.dropdown('newReportDateRangeDropdown', [
                    { value: 'today', label: 'Today' },
                    { value: 'last_7_days', label: 'Last 7 days' },
                    { value: 'last_30_days', label: 'Last 30 days' }
                ], 'last_30_days')
            )}
            ${Components.formField('newReportPageType', 'Page type filter',
                Components.dropdown('newReportPageTypeDropdown', [
                    { value: 'all', label: 'All page types' },
                    ...PAGE_TYPES.map(t => ({ value: t, label: t.charAt(0).toUpperCase() + t.slice(1) }))
                ], 'all')
            )}
        `;
        const footer = `
            <button class="btn btn-secondary" data-testid="modal-cancel" onclick="Components.closeModal()">Cancel</button>
            <button class="btn btn-primary" data-testid="submit-create-report" id="submitCreateReport">Save Report</button>
        `;
        Components.showModal('Save Custom Report', body, footer);

        setTimeout(() => {
            document.getElementById('submitCreateReport').addEventListener('click', () => {
                const name = document.getElementById('newReportName').value.trim();
                const metric = document.getElementById('newReportMetricDropdown').getAttribute('data-value') || 'lcp';
                const reportType = document.getElementById('newReportTypeDropdown').getAttribute('data-value') || 'over_time';
                const deviceType = document.getElementById('newReportDeviceTypeDropdown').getAttribute('data-value') || 'all';
                const dateRange = document.getElementById('newReportDateRangeDropdown').getAttribute('data-value') || 'last_30_days';
                const pageType = document.getElementById('newReportPageTypeDropdown').getAttribute('data-value') || 'all';

                if (!name) {
                    Components.showToast('Please enter a report name', 'error');
                    return;
                }

                AppState.addSavedReport({ name, metric, reportType, filters: { deviceType, dateRange, pageType } });
                Components.closeModal();
                Components.showToast('Report saved', 'success');
                Router.refresh();
            });
        }, 50);
    },

    // ---- Helper ----
    _appColor(category) {
        const colors = {
            'Reviews': '#6366f1', 'Marketing': '#ec4899', 'Conversion': '#f59e0b',
            'Analytics': '#06b6d4', 'Social Media': '#8b5cf6', 'Page Builder': '#10b981'
        };
        return colors[category] || '#6b7280';
    },

    _notFound(message) {
        return `
            <div class="page-header">
                <h1 class="page-title">Not Found</h1>
            </div>
            <div class="card mt-md">
                <div class="card-body text-center">
                    <p class="text-muted">${Components.escapeHtml(message || 'The page you\'re looking for doesn\'t exist.')}</p>
                    <div class="mt-md">
                        <a href="#/" data-route="/" class="btn btn-primary">Go to Dashboard</a>
                    </div>
                </div>
            </div>
        `;
    }
};
