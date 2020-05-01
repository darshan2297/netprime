from django.contrib import admin

# Register your models here.
from NP_admin.models import (
    register_admin,main_catagory,sub_catagory,type_catagory,movie_content,
    webseries_content,movies_csv_content,webseries_season,webseries_season_episode,cast,crew,movies_watchlist,movie_review,webseries_review,webseries_watchlist,Transaction,renewmember,
    language,multiple_audio_movies
    )

admin.site.register(register_admin)
admin.site.register(main_catagory)
admin.site.register(sub_catagory)
admin.site.register(type_catagory)
admin.site.register(movie_content)
admin.site.register(language)
admin.site.register(multiple_audio_movies)
admin.site.register(webseries_content)
admin.site.register(webseries_season)
admin.site.register(webseries_season_episode)
admin.site.register(cast)
admin.site.register(crew)
admin.site.register(movies_watchlist)
admin.site.register(movie_review)
admin.site.register(webseries_watchlist)
admin.site.register(webseries_review)
admin.site.register(Transaction)
admin.site.register(renewmember)
admin.site.register(movies_csv_content)
