from rest_framework import routers
from library.api_views import BookViewset


router = routers.DefaultRouter()
router.register('books', BookViewset, basename='books')
# router.register('delete', BookViewset, basename='delete')