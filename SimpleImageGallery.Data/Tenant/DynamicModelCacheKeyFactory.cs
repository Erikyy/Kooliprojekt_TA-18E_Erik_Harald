using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using System;
using System.Collections.Generic;
using System.Text;

namespace SimpleImageGallery.Data
{
    public class DynamicModelCacheKeyFactory : IModelCacheKeyFactory

    {

        public object Create(DbContext context)

        {

            if (context is SimpleImageGalleryDbContext dynamicContext)

            {

                return new { dynamicContext.TenantId };

            }



            throw new Exception("Unknown DBContext type");

        }

    }
}
