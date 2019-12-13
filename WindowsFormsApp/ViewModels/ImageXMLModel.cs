using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Xml.Serialization;

namespace WindowsFormsApp.ViewModels
{
    internal class ImageXMLModel : IImagemodel
    {
        private readonly string _xmlFilePath;
        private readonly XmlSerializer _serializer = new XmlSerializer(typeof(List<Image>));
        private readonly Lazy<List<Image>> _images;

        public ImageXMLModel(string fullPath)
        {
            _xmlFilePath = fullPath + @"\images.xml";

            if (!File.Exists(_xmlFilePath))
                CreateImageXmlStub();

            _images = new Lazy<List<Image>>(() =>
            {
                using (var reader = new StreamReader(_xmlFilePath))
                {
                    return (List<Image>)_serializer.Deserialize(reader);
                }
            });
        }
        private void CreateImageXmlStub()
        {
            var stubImageList = new List<Image> { 
                //here goes xml content
            };
            SaveImageList(stubImageList);
        }
        private void SaveImageList(List<Image> images)
        {
            using(var writer = new StreamWriter(_xmlFilePath, false))
            {
                _serializer.Serialize(writer, images);
            }
        }
        public IEnumerable<Image> GetAllImages()
        {
            return _images.Value;
        }
        public Image GetImage(int id)
        {
            return _images.Value[id];
        }
        public void SaveImage(int id, Image image)
        {
            _images.Value[id] = image;
            SaveImageList(_images.Value);

        }
    }
}
