from django.urls import path
from . import views
from .views import * 



# plot_view, add_plot_view, delete_plot_view, edit_plot_view, my_plots_view, like_plot, like_comment, search_plots_view, search_categories_view, campsite_plots_view, wild_plots_view, official_plots_view, search_countries_view, country_view, comment_sent, delete_comment, reply_sent, delete_reply, questions_view, report_plot_view, check_reports_view

urlpatterns = [
    path("", views.home, name="home"),
    path("show_plot/<plot_id>/", plot_view, name="show-plot"),  # noqa: F405
    path("add_plot/", add_plot_view, name="add-plot"),  # noqa: F405
    path("delete_plot/<pk>/", delete_plot_view, name="delete-plot"),  # noqa: F405
    path("edit_plot/<pk>/", edit_plot_view, name="edit-plot"),  # noqa: F405
    path("my_plots/", my_plots_view, name="my-plots"),  # noqa: F405
    path("myplots/", my_plots_view, name="my-plots"),  # noqa: F405
    path("plot/like/<pk>/", like_plot, name="like-plot"),  # noqa: F405
    path("comment/like/<pk>/", like_comment, name="like-comment"),  # noqa: F405
    path("search_plots/", search_plots_view, name="search-plots"),  # noqa: F405
    path("search_campsites/", search_campsites_view, name="search-campsites"),  # noqa: F405
    path("campsite_plots/", campsite_plots_view, name="campsite-plots"),  # noqa: F405
    path("wild_plots/", wild_plots_view, name="wild-plots"),  # noqa: F405
    path("official_plots/", official_plots_view, name="official-plots"),  # noqa: F405
    path("search_countries/", search_countries_view, name="search-countries"),  # noqa: F405
    path("country/<plot_country>/", country_view, name="country"),  # noqa: F405
    path("commentsent/<pk>/", comment_sent, name="comment-sent"),  # noqa: F405
    path("delete_comment/<pk>/", delete_comment, name="delete-comment"),  # noqa: F405
    path("replysent/<pk>/", reply_sent, name="reply-sent"),  # noqa: F405
    path("delete_reply/<pk>/", delete_reply, name="delete-reply"),  # noqa: F405
    path("questions/", questions_view, name="questions"),  # noqa: F405
    path("report_plot/<pk>/", report_plot_view, name="report-plot"),  # noqa: F405
    path("check_reports/", check_reports_view, name="check-reports"),  # noqa: F405
    path("about/", about_view, name="about"),  # noqa: F405
    path("plot_table/", plot_table_view, name="plot-table"),  # noqa: F405
]