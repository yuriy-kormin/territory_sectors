from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.db.models import Count
from PIL import Image
from io import BytesIO


class CountFlatsMixin:
    def get_queryset(self):
        qs = super(CountFlatsMixin, self).get_queryset()
        return qs.annotate(Count('flat'))

    # def get_context_data(self, **kwargs):
    #     query = self.get_queryset()
    #     context = super().get_context_data(**kwargs)
    #     obj = self.model
    #     context[object] = House.objects.filter(
    #         flat__in=query
    #     ).distinct().annotate(Count('flat'))
    #
    #     return context


# class LanguagesListMixin:
#     def get_con(self):
#         qs = super(CountFlatsMixin, self).get_queryset()
#         return qs.annotate(Count('flat'))
class PaginateMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)
        context['page_obj'] = page_obj
        return context


class ImageResizeBeforeMixin:
    def form_valid(self, form):
        image = form.cleaned_data.get('image')
        if image:
            img = Image.open(image)
            width, height = img.size
            if width > height:
                new_width = self.model.MAX_IMAGE_RESOLUTION
                new_height = int(height * (new_width / width))
            else:
                new_height = self.model.MAX_IMAGE_RESOLUTION
                new_width = int(width * (new_height / height))
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img = img.convert('RGB')
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=90)

            image_data = buffer.getvalue()
            # fix here: pass image.name as the first argument instead of 'image'
            form.instance.image.save(image.name, content=ContentFile(image_data), save=False)

        return super().form_valid(form)
