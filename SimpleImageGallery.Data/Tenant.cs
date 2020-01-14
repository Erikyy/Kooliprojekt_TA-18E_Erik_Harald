using System;
using System.Collections.Generic;
using System.Text;

namespace SimpleImageGallery.Data
{
    public class Tenant

    {
        public int Id { get; set; }
        public int DatabaseType { get; set; }
        public string Host { get; set; }
        public string ConnectionString { get; set; }
        public string Name { get; set; }
    }
}
