using Newtonsoft.Json;
using SimpleImageGallery.Controllers;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;



namespace WpfApp.HttpClient
{
    public class Client
    {
        private const string BaseUrl = "http://localhost:59852/api/";

        public System.Net.Http.HttpClient client = new System.Net.Http.HttpClient();

        public async Task<IList<ImageController>> List(int page)

        {

            using (client)

            {

                var json = await client.GetStringAsync(BaseUrl + "List?page=" + page);



                return JsonConvert.DeserializeObject<List<ImageController>>(json);

            }

        }
    }
}
