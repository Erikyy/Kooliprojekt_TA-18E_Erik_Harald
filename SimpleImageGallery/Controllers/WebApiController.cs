using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Dynamic.Core;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using SimpleImageGallery.Data;

namespace SimpleImageGallery.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class WebApiController : ControllerBase
    {
        private readonly SimpleImageGalleryDbContext _datacontext;

        public WebApiController(SimpleImageGalleryDbContext datacontext)
        {
            _datacontext = datacontext;
        }
        
        public async Task<IList<ImageController>>List(int page)
        {
            var PagedResult = new List<ImageController>();

            return await Task.FromResult(PagedResult);


        }

        
    }
}
