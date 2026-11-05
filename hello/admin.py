from django.contrib import admin
from .models import User, Category, Product


def dashboard_callback(request, context):
    """Добавляет статистику на главную страницу админки"""
    context.update({
        "stats": {
            "total_products": Product.objects.count(),
            "total_categories": Category.objects.count(),
            "total_users": User.objects.count(),
        }
    })
    return context


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    inlines = [ProductInline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'patronymic')
    list_display_links = ('id', 'surname')
    search_fields = ('name', 'surname', 'patronymic')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'sale', 'material', 'date_prod', 'counter')
    list_display_links = ('id', 'name')
    list_filter = ('category', 'material', 'date_prod')
    search_fields = ('name', 'material')
    list_editable = ('sale', 'counter')
    