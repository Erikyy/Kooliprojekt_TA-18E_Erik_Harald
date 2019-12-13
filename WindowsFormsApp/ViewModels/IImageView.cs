using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp.ViewModels
{
    public interface IImageView
    {
        IList<string> ImageList { get; set; }
        int SelectedImage { get; set; }
        string Title { get; set; }
        string Tags { get; set; }

        presenter.presenter presenter { set; }

    }
}
