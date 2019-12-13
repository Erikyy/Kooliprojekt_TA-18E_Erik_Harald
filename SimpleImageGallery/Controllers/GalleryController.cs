using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using SimpleImageGallery.Data;
using SimpleImageGallery.Data.Models;
using SimpleImageGallery.Models;

namespace SimpleImageGallery.Controllers
{
    public class GalleryController : Controller
    {
        private readonly IImage _imageService;
        public GalleryController(IImage imageService) 
        {
            _imageService = imageService;
        }

        public IActionResult Index(string searchQuery = "")
        {
            IEnumerable<GalleryImage> imageList;
            if(searchQuery != "")
            {
                imageList = _imageService.SearchImage(searchQuery);
            }
            else
            {
                imageList = _imageService.GetAll();
            }

            if (!imageList.Any())
            {
                return View("NoImages");
            }

            var model = new GalleryIndexModel()
            {
                Images = imageList,
                SearchQuery = searchQuery
            };

            return View(model); 
        }

        public IActionResult Column() 
        {
            return Index();
        }

        public IActionResult Large()
        {
            return Index();
        }
        public IActionResult Table()
        {
            return Index();
        }

        public IActionResult Detail(int id)
        {
            var image = _imageService.GetById(id);

            var model = new GalleryDetailModel()
            {
                Id = image.Id,
                Title = image.Title,
                CreatedOn = image.Created,
                Url = image.Url,
                Tags = image.Tags.Select(t => t.Description).ToList()
            };

            return View(model);
        }
    }
}