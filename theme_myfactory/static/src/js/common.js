/*
 * Match Height
 */
;;(function($){
    var viewport = {
        width: Math.max(document.documentElement.clientWidth, window.innerWidth || 0),
        height: Math.max(document.documentElement.clientHeight, window.innerHeight || 0)
    }


    $(function(){
        switch(true){
            case viewport.width >= 1200:
                //runMatchHeight('lg');
            case viewport.width >= 992:
                runMatchHeight('md');
            case viewport.width >= 768:
                //runMatchHeight('sm');
            default:
                //runMatchHeight('xs');
        }
    });

    // Helper: Evoke match height by group
    // Base on viewport group
    function runMatchHeight(viewportGroup){

        if(!viewportGroup)
            return;

        var groups = {};

        // generate groups by their groupId set by elements using data-match-height
        $('[data-mh-' + viewportGroup + ']').each(function() {
            var $this = $(this),
                groupId = $this.attr('data-mh-' + viewportGroup);

            if (groupId in groups) {
                groups[groupId] = groups[groupId].add($this);
            } else {
                groups[groupId] = $this;
            }
        });

        // apply matchHeight to each group
        $.each(groups, function() {
            this.matchHeight(true);
        });
    }
})(jQuery);

/*
 * Scroll to anchor
 */
(function($, window, document, history){

    // When everything is loaded
    $(window).on('load',function(){
        $(window).on('hashchange', function(e){

            e.preventDefault();

            var selector = e.fragment || '',
                $target = $('#' + selector);

            if(!$target.length)
                return;

            var offset = parseFloat($target.data('offset')) || 0;
            $('html, body').animate({
                scrollTop: $target.offset().top + offset
            }, 500);

            return false;
        });

        if(document.location.hash)
            $(window).trigger('hashchange');
    });

    $(function(){

        $('.js-scroll-to').on('click', function(e){

            var selector = this.hash || $(this).data('scroll-target') || '',
                $target = $(selector);

            if(!$target.length)
                return;

            // Change hash
            if(history)
                history.replaceState({}, '', this.href);

            var offset = parseFloat($target.data('offset')) || 0;
            $('html, body').animate({
                scrollTop: $target.offset().top + offset
            }, 500);

            return false;
        });
    });
})(jQuery, window, document, history || false);

/*
 * Selectric
 */
(function($){
    $(function(){
        $('.selectric').selectric();
    })
})(jQuery);

/*
 * Contact Form
 */
(function($){
    $(function(){

        /* Parsley.js */
        form = $('#form-contact-us').parsley({
            errorClass: 'has-error',
            successClass: 'has-success',
            classHandler: function(field){
                return field.$element.closest('.form-group');
            },
            errorsWrapper: '<ul class="parsley-errors-list"></ul>',
            errorTemplate: '<li class="help-block"></li>'
        });
    })
})(jQuery);