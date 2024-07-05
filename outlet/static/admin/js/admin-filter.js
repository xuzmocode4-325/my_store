(function($) {
    $(document).ready(function() {
        var categorySelect = $('#id_category');
        var subcategorySelect = $('#id_subcategory');
        var itemTypeSelect = $('#id_item_type');

        function updateSubcategories() {
            var categoryId = categorySelect.val();
            subcategorySelect.find('option').hide();
            subcategorySelect.find('option[data-category-id="' + categoryId + '"]').show();
            subcategorySelect.val('');
        }

        function updateItemTypes() {
            var subcategoryId = subcategorySelect.val();
            itemTypeSelect.find('option').hide();
            itemTypeSelect.find('option[data-subcategory-id="' + subcategoryId + '"]').show();
            itemTypeSelect.val('');
        }

        categorySelect.change(updateSubcategories);
        subcategorySelect.change(updateItemTypes);

        // Initialize fields on page load
        updateSubcategories();
        updateItemTypes();
    });
})(django.jQuery);