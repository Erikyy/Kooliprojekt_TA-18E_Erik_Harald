using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Wpf_App.HttpClient
{
    public class HttpClient
    {
        private const string BaseUrl = "http://localhost:59852/api/";



        public async Task<IList<>> List(int page)

        {

            using (var client = new HttpClient())

            {

                var json = await client.GetStringAsync(BaseUrl + "List?page=" + page);



                return JsonConvert.DeserializeObject<List<InvoiceListItem>>(json);

            }

        }
    }
}
