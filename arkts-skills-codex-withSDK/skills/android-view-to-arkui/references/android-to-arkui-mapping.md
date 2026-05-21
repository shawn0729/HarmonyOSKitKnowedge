# Android View/XML To ArkUI Mapping

Use this file when translating source Android UI structures into ArkUI components.

## Page And Shell Mapping

| Android source | ArkUI target | Notes |
| --- | --- | --- |
| `Activity` | routed page or app shell page | Use for top-level destinations and window-level state. |
| `Fragment` | reusable `@Component` or routed page | Promote to page only if it is a top-level destination. |
| `DialogFragment` / dialog class | dialog or sheet component | Keep the dialog separate from the page. |
| `DrawerLayout` | shell-level navigation container | Build once in the app shell, not per page. |
| `BottomNavigationView` | shell tabs or bottom navigation component | Centralize routing and tab state. |
| `FragmentContainerView` | child component slot | Use parent/child composition instead of recreating Android fragment transactions. |

## Layout Mapping

| Android source | ArkUI target | Notes |
| --- | --- | --- |
| `LinearLayout` vertical | `Column` | Prefer extracted child components over deep nesting. |
| `LinearLayout` horizontal | `Row` | |
| `FrameLayout` | `Stack` | Good for overlay content. |
| `RelativeLayout` | `Stack`, `Row`, `Column` | Restructure instead of trying to mirror each rule mechanically. |
| `ConstraintLayout` | split into smaller ArkUI components | Mechanical translation is usually fragile. |
| `NestedScrollView` / `ScrollView` | `Scroll` | Keep one main scroll owner per page when possible. |
| `SwipeRefreshLayout` | refresh wrapper or placeholder refresh action | If target refresh behavior is unclear, preserve the action path first. |
| `CoordinatorLayout` | page shell + explicit state | Do not try to reproduce Android behavior nesting blindly. |

## Control Mapping

| Android source | ArkUI target | Notes |
| --- | --- | --- |
| `TextView` | `Text` | |
| `ImageView` | `Image` | |
| `Button` / `MaterialButton` | `Button` | Preserve emphasis levels rather than exact class names. |
| `Toolbar` / `MaterialToolbar` | page header component | Convert menu items into explicit actions. |
| `RecyclerView` | `List`, `Grid`, `Scroll`, `ForEach`, or `LazyForEach` | Always extract an item component. |
| `Adapter` + `ViewHolder` | item component + callbacks | The adapter is a structural dependency, not a target artifact. |
| menu XML | header actions or contextual action area | Do not silently drop actions. |
| XML item layout | ArkUI child component | One item layout should map to one reusable component where possible. |

## Resource Mapping

| Android source | ArkUI target | Notes |
| --- | --- | --- |
| `strings.xml` | resources or constants | Keep display text out of page logic where possible. |
| colors, dimens | ArkUI resources or design tokens | Normalize repeated values into tokens first. |
| `dp` | `vp` | Convert size intent, not just raw numbers. |
| `sp` | `fp` | |
| styles and themes | shared tokens and shell-level theme setup | Do not mirror Android style names one-to-one. |

## Migration Rules

- Translate page shell, page content, list items, dialogs, and sections as separate target artifacts.
- If the source page mixes empty state, list state, and loading state, keep those states explicit in ArkUI rather than flattening to one static layout.
- If the source page injects children dynamically, convert that to explicit component composition with clear props.
- If one source XML is reused in multiple contexts, create a shared ArkUI component instead of duplicating it.
- If the source uses view binding or data binding, treat the binding class as a clue for layout dependency discovery.

## Suggested Target Structure

Use a structure close to this when the target project is still empty:

- `entry/src/main/ets/pages/` for routed pages
- `entry/src/main/ets/components/` for reusable page parts, cards, dialogs, and list items
- `entry/src/main/ets/models/` for UI-facing data shapes
- `entry/src/main/ets/viewmodels/` or state helpers for local page state
- `entry/src/main/resources/` for strings, colors, media, and profile config

Keep shell components separate from feature pages.
