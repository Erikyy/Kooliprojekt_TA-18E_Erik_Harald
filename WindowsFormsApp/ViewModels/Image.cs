using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp.ViewModels
{
    public class Image
    {
        public string Title { get; set; }

        public string Tags { get; set; }

        public override bool Equals(object obj)
        {
            Image other = obj as Image;
            return Equals(other);
        }
        public override int GetHashCode()
        {
            return Title.GetHashCode()
                ^ Tags.GetHashCode();
        }
        public bool Equals(Image other)
        {
            if(other == null)
            {
                return false;

            }
            return this.Title == other.Title
                && this.Tags == other.Tags;
        }
    }
}
