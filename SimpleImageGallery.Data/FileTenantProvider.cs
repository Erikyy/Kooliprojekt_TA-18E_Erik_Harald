using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;

namespace SimpleImageGallery.Data
{
    public class FileTenantProvider : ITenantProvider

    {

        private static Tenant[] _tenants = new Tenant[] { };

        private string _host;

        public FileTenantProvider(IHttpContextAccessor accessor)

        {
            _host = accessor.HttpContext.Request.Host.ToString();
        }

        public Tenant GetTenant()

        {
            LoadTenants();

            return _tenants.FirstOrDefault(t => t.Host.ToLower() == _host.ToLower());
        }
        private static void LoadTenants()
        {
            if (_tenants != null && _tenants.Length > 0)

            {
                return;
            }
            var tenants = File.ReadAllText("tenants.json");

            _tenants = JsonConvert.DeserializeObject<Tenant[]>(tenants);

        }

        public Tenant[] ListTenants()

        {
            return _tenants;
        }

    }
}
