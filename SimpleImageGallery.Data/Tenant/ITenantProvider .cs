using System;
using System.Collections.Generic;
using System.Text;

namespace SimpleImageGallery.Data
{
    public interface ITenantProvider
    {
        Tenant GetTenant();

        Tenant[] ListTenants();

    }
}
