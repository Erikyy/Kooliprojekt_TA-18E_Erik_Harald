$(document).ready(function() {
    var $jg = $('.justified-gallery');
    if ($jg.length) {
        $jg.justifiedGallery({
            rowHeight: 200
        }).on('jg.complete', function() {
            $jg.lightGallery({
                thumbnail: false,
                share: false
            }); 
        });
    } else {
        var $pictures = $('.pictures');
        if ($pictures.length) {
            $pictures.lightGallery({
                thumbnail: false,
                share: false
            });
        }
    }
});