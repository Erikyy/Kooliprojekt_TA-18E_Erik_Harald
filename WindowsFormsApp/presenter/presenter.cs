using System.Linq;
using WindowsFormsApp.ViewModels;



namespace WindowsFormsApp.presenter
{
    public class presenter
    {
        private readonly IImageView _view;
        private readonly IImagemodel _imagemodel;

        public presenter(IImageView view, IImagemodel repository)
        {
            _view = view;
            view.presenter = this;
            _imagemodel = repository;

            UpdateImageListView();
        }

        private void UpdateImageListView()
        {
            var imageNames = from image in _imagemodel.GetAllImages() select image.Title;
            int selectedImage = _view.SelectedImage >= 0 ? _view.SelectedImage : 0;
            _view.ImageList = imageNames.ToList();
            _view.SelectedImage = selectedImage;
        }

        public void UpdateImageView(int p)
        {
            
            Image image = _imagemodel.GetImage(p);
            _view.Title = image.Title;
            _view.Tags = image.Tags;
           
        }

        public void SaveCustomer()
        {
            Image image = new Image { Title = _view.Title, Tags = _view.Tags};
            _imagemodel.SaveImage(_view.SelectedImage, image);
            UpdateImageListView();
        }
    }
}
