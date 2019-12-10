// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.
$(document).ready(function () {
    var $jg = $('.justified-gallery');
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
        var $pictures = $('.pictures');
        if ($pictures.length) {
            $pictures.lightGallery({
                thumbnail: false,
                share: false
            });
        }
    }
});