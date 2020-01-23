from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet
from . import models


class AuthorContainerForm(ModelForm):
    class Meta:
        model = models.AuthorContainer
        exclude = ('id',)


class AuthorForm(ModelForm):
    class Meta:
        model = models.Author
        fields = ('first_name', 'last_name', 'email')



class BookForm(ModelForm):
    class Meta:
        model = models.Book

        fields = ('title', 'isbn',)



BookFormset = inlineformset_factory(models.Author, models.Book, form=BookForm, can_delete=True, extra=0)


class BaseAuthorFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseAuthorFormset, self).add_fields(form, index)
        form.nested_book = BookFormset(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix='nested_book-%s-%s' % (
                form.prefix,
                BookFormset.get_default_prefix()))

    def is_valid(self):
        result = super(BaseAuthorFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested_book'):
                    result = result and form.nested_book.is_valid()

        return result

    def save(self, commit=True):
        result = super(BaseAuthorFormset, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested_book'):
                if not self._should_delete_form(form):
                    form.nested_book.save(commit=commit)
        return result


AuthorsFormset = inlineformset_factory(models.AuthorContainer, models.Author, formset=BaseAuthorFormset,
                                       form=AuthorForm, extra=0)
