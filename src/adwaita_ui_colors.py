from adwaita_colors import get_adwaita_colors


named_colors, _syntax_colors = get_adwaita_colors()


def get_adwaita_ui_colors():
    def _(name): return lambda value: named_colors[f'{name}_{value}']

    ui_colors = {
        # libadwaita doesn't use shadows to indicate scrollable content.
        'scrollbar.shadow':                     '#00000000',

        'activityBar.background':               '#303030',
        'titleBar.activeBackground':            '#303030',
        'tab.activeBackground':                 '#303030',
        'tab.inactiveBackground':               '#262626',
        'editorGroupHeader.tabsBackground':     '#262626',
        'breadcrumb.background':                '#262626',
        'tab.hoverBackground':                  '#363636',
        # 'tab.activeForeground':               '#ffffff'
        # 'tab.inactiveForeground':             '#cccccc'

        'panel.background':                     '#242424',
        'sideBar.background':                   '#242424',
        'statusBar.background':                 '#242424',
        'statusBar.noFolderBackground':         '#242424',
        'statusBarItem.remoteBackground':       '#242424',
        'panelSectionHeader.background':        '#00000000',
        'sideBarSectionHeader.background':      '#00000000',

        'activityBar.border':                   '#454545',
        'editorBracketMatch.border':            '#454545',
        'editorGroup.border':                   '#454545',
        'editorGroupHeader.border':             '#454545',
        'editorGroupHeader.tabsBorder':         '#454545',
        'panel.border':                         '#454545',
        'panelSectionHeader.border':            '#454545',
        'sideBar.border':                       '#454545',
        'sideBarSectionHeader.border':          '#454545',
        'statusBar.border':                     '#454545',
        'tab.border':                           '#454545',
        'titleBar.border':                      '#454545',
        'window.activeBorder':                  '#454545',
        'tree.indentGuidesStroke':              '#45454599',
        'editorIndentGuide.activeBackground':   '#45454599',
        'editorIndentGuide.background':         '#45454580',
        'editorRuler.foreground':               '#45454580',
        'editorBracketMatch.background':        '#45454520',
        # A dotted outline, not a solid border, but it's the best we can get.
        # 'list.inactiveFocusOutline':            '#454545',

        'list.hoverBackground':                 '#333333',
        'list.inactiveSelectionBackground':     '#3a3a3a',
        'input.background':                     '#3a3a3a',

        # #323232 is from libadwaita. For dark theme most text is #fff, but in VS Code there's way
        # more text displayed at the same time, so I find a softer color works better.
        'statusBar.foreground':                 '#cccccc',
        'statusBar.noFolderForeground':         '#cccccc',
        'statusBar.debuggingForeground':        '#cccccc',
        'statusBarItem.remoteForeground':       '#cccccc',
        'sideBar.foreground':                   '#cccccc',
        'panelTitle.activeBorder':              '#cccccc',
        'panelTitle.activeForeground':          '#cccccc',

        'activityBar.activeBorder':             '#00000000',
        'activityBarBadge.background':          _('blue')(3),
        'button.background':                    _('blue')(3),
        # A border of the same color makes buttons slightly taller.
        'button.border':                        _('blue')(3),
        'list.activeSelectionBackground':       _('blue')(6),
        'list.highlightForeground':             '#ffffff',
        'list.activeSelectionForeground':       '#ffffff',
        'list.activeSelectionIconForeground':   '#ffffff',
        'list.focusHighlightForeground':        '#ffffff',


        'editorGutter.addedBackground':                     _('green')(6),
        'editorGutter.deletedBackground':                   _('red')(5),
        'editorGutter.modifiedBackground':                  _('blue')(5),
        'gitDecoration.addedResourceForeground':            _('green')(1) + 'dd',
        'gitDecoration.renamedResourceForeground':          _('green')(1) + 'dd',
        'gitDecoration.untrackedResourceForeground':        _('green')(1) + 'dd',
        'gitDecoration.modifiedResourceForeground':         _('orange')(1) + 'dd',
        'gitDecoration.stageModifiedResourceForeground':    _('orange')(1) + 'dd',
        'gitDecoration.deletedResourceForeground':          _('red')(1) + 'dd',
        'gitDecoration.stageDeletedResourceForeground':     _('red')(1) + 'dd',
        'gitDecoration.ignoredResourceForeground':          _('dark')(1),

        # Color-picked colors
        'commandCenter.background':             '#444444',
        'commandCenter.border':                 '#00000000',
        'button.hoverBackground':               '#4990e7',
        'focusBorder':                          '#5f7999',

        # Hand-picked colors
        'activityBar.foreground':               '#ffffff',
        'editor.background':                    '#1d1d1d',
        'editorLineNumber.foreground':          '#666666',
        'widget.shadow':                        '#00000033',
    }

    return ui_colors
