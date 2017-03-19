;;(function($){
    var viewport = {
        width: Math.max(document.documentElement.clientWidth, window.innerWidth || 0),
        height: Math.max(document.documentElement.clientHeight, window.innerHeight || 0)
    }

    // It is md screen
    if(viewport.width >= 992){

        $(function(){

            var groups = {};

            // generate groups by their groupId set by elements using data-match-height
            $('[data-mh-md]').each(function() {
                var $this = $(this),
                    groupId = $this.attr('data-mh-md');

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
        });
    }
})(jQuery);