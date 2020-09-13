$(document).ready(function () {
    let $jg = $('.justified-gallery');
    if ($jg.length) {
        $jg.justifiedGallery({
            rowHeight: 200
        }).on('jg.complete', function () {
            $jg.lightGallery({
                thumbnail: false,
                share: false
            });
        });
    } else {
        let $pictures = $('.pictures');
        if ($pictures.length) {
            $pictures.lightGallery({
                thumbnail: false,
                share: false
            });
        }
    }
});