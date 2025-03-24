import pytest
import matplotlib
matplotlib.use('Agg')  # backend bezinterfejsowy (brak okna), przydatny w CI/CD
from ZADANIE3.main import draw_scatter_plot

def test_draw_scatter_plot_return_type():
    """
    Sprawdzamy, czy draw_scatter_plot zwraca obiekt Figure.
    """
    fig = draw_scatter_plot()
    assert isinstance(fig, matplotlib.figure.Figure), "Funkcja powinna zwracać obiekt Figure."


def test_draw_scatter_plot_axes():
    """
    Sprawdzamy, czy zwrócona figura ma co najmniej jedną oś (Axes).
    """
    fig = draw_scatter_plot()
    axes = fig.get_axes()
    assert len(axes) > 0, "Wykres powinien zawierać co najmniej jedną oś (Axes)."

    ax = axes[0]
    assert ax.get_title() != "", "Oś powinna mieć ustawiony tytuł (np. 'Wykres punktowy')."


def test_draw_scatter_plot_points():
    """
    Sprawdzamy, czy wykres zawiera obiekt typu PathCollection,
    co wskazuje na istnienie punktów (scatter).
    """
    fig = draw_scatter_plot()
    ax = fig.get_axes()[0]
    children = ax.get_children()

    from matplotlib.collections import PathCollection
    scatter_found = any(isinstance(ch, PathCollection) for ch in children)
    assert scatter_found, "Nie znaleziono żadnych punktów typu scatter na wykresie."


def test_draw_scatter_plot_labels():
    """
    Sprawdzamy, czy osie są podpisane.
    """
    fig = draw_scatter_plot()
    ax = fig.get_axes()[0]
    xlabel = ax.get_xlabel()
    ylabel = ax.get_ylabel()
    assert xlabel != "", "Oś X powinna mieć etykietę."
    assert ylabel != "", "Oś Y powinna mieć etykietę."
