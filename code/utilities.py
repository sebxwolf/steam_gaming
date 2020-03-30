from import_packages import *
from start_spark import git

# Function to style the cells of a crosstab table
def crosstab_plot(df, title = "Crosstab", color = "#2ecc71"):
    cm = sns.light_palette(color, as_cmap=True)
    styles = [dict(selector="th",
                props=[("font-size", "90%"),
                    ("text-align", "right"),
                    ("background-color", "#edf9f2")]),
                dict(selector="caption",
                     props=[("font-size", "150%"),
                           ("color", "black")])]
    temp = df.style.background_gradient(cmap=cm) \
                    .set_caption(title) \
                    .set_table_styles(styles)
    return temp.format('{:,.0f}')

# Function that takes a df, main var and pivot vars and returns a list of crosstab dfs
def crosstab_list_count(df, main_var, list_of_pivot_vars, title):
    dfs = {}
    style_dfs = {}
    for i in list_of_pivot_vars:
        temp = df.groupBy(main_var) \
              .pivot(i) \
              .count() \
              .toPandas() \
              .fillna(0) \
              .sort_values(main_var) \
              .set_index(main_var)
        dfs[i] =  temp
        style_dfs[i] = crosstab_plot(temp,
              title + i)
        #temp.to_csv('../csv_outputs/' + main_var + i + 'crosstab.csv')
    return dfs, style_dfs

class SeabornFig2Grid():

    def __init__(self, seaborngrid, fig,  subplot_spec):
        self.fig = fig
        self.sg = seaborngrid
        self.subplot = subplot_spec
        if isinstance(self.sg, sns.axisgrid.FacetGrid) or \
            isinstance(self.sg, sns.axisgrid.PairGrid):
            self._movegrid()
        elif isinstance(self.sg, sns.axisgrid.JointGrid):
            self._movejointgrid()
        self._finalize()

    def _movegrid(self):
        """ Move PairGrid or Facetgrid """
        self._resize()
        n = self.sg.axes.shape[0]
        m = self.sg.axes.shape[1]
        self.subgrid = gridspec.GridSpecFromSubplotSpec(n,m, subplot_spec=self.subplot)
        for i in range(n):
            for j in range(m):
                self._moveaxes(self.sg.axes[i,j], self.subgrid[i,j])

    def _movejointgrid(self):
        """ Move Jointgrid """
        h= self.sg.ax_joint.get_position().height
        h2= self.sg.ax_marg_x.get_position().height
        r = int(np.round(h/h2))
        self._resize()
        self.subgrid = gridspec.GridSpecFromSubplotSpec(r+1,r+1, subplot_spec=self.subplot)

        self._moveaxes(self.sg.ax_joint, self.subgrid[1:, :-1])
        self._moveaxes(self.sg.ax_marg_x, self.subgrid[0, :-1])
        self._moveaxes(self.sg.ax_marg_y, self.subgrid[1:, -1])

    def _moveaxes(self, ax, gs):
        #https://stackoverflow.com/a/46906599/4124317
        ax.remove()
        ax.figure=self.fig
        self.fig.axes.append(ax)
        self.fig.add_axes(ax)
        ax._subplotspec = gs
        ax.set_position(gs.get_position(self.fig))
        ax.set_subplotspec(gs)

    def _finalize(self):
        plt.close(self.sg.fig)
        self.fig.canvas.mpl_connect("resize_event", self._resize)
        self.fig.canvas.draw()

    def _resize(self, evt=None):
        self.sg.fig.set_size_inches(self.fig.get_size_inches())
