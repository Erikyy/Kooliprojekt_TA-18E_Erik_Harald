using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace SimpleImageGallery.Data
{
    public static class DataGenerator

    {

        public static void GenerateData(this SimpleImageGalleryDbContext dbContext, int tenantId)

        {

            if (tenantId == 1)

            {

                GenerateForTenant1(dbContext);

            }

            if (tenantId == 2)

            {

                GenerateForTenant2(dbContext);
            }

            if (tenantId == 3)

            {

                GenerateForTenant3(dbContext);

            }
        }
        private static void GenerateForTenant1(SimpleImageGalleryDbContext dbContext)

        {
            // Tenant1 andmete loomine 
        }


        private static void GenerateForTenant2(SimpleImageGalleryDbContext dbContext)

        {

            // Tenant2 andmete loomine 

        }



        private static void GenerateForTenant3(SimpleImageGalleryDbContext dbContext)

        {

            // Tenant3 andmete loomine 

        }

    }
}
