using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp.ViewModels
{
    public interface IImagemodel
    {
        IEnumerable<Image> GetAllImages();

        Image GetImage(int id);

        void SaveImage(int id, Image image);

        
    }
}
