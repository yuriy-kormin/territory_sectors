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
        def calculate_new_size(max_size, width, height):
            if width > height:
                return max_size, int(height * (max_size / width))
            return int(width * (max_size / height)), max_size

        def process_rotation_based_on_exif(img):
            exif = img._getexif()
            # if image has exif data about orientation, let's rotate it
            orientation_key = 274  # cf ExifTags
            if exif and orientation_key in exif:
                orientation = exif[orientation_key]

                rotate_values = {
                    3: Image.ROTATE_180,
                    6: Image.ROTATE_270,
                    8: Image.ROTATE_90
                }

                if orientation in rotate_values:
                    img = img.transpose(rotate_values[orientation])

        def resize_image(image_data, max_size):
            with Image.open(image_data) as img:
                process_rotation_based_on_exif(img)
                image_dimensions = calculate_new_size(max_size, *img.size)
                img = img.resize(image_dimensions, Image.ANTIALIAS)
                img = img.convert('RGB')
                buffer = BytesIO()
                img.save(buffer, format='JPEG', quality=90)
            return buffer.getvalue()

        image = form.cleaned_data.get('image')
        if image:
            image_data = resize_image(
                image, form.instance.MAX_IMAGE_RESOLUTION)
            form.instance.image.save(
                image.name, content=ContentFile(image_data), save=False)
            image_data = resize_image(
                image, form.instance.PREVIEW_IMAGE_RESOLUTION)
            form.instance.image_preview.save(
                image.name, content=ContentFile(image_data), save=False)

        return super().form_valid(form)
