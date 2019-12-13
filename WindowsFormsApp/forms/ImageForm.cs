using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp.forms
{
    public partial class ImageForm : Form
    {
        private bool _isEditMode = false;
        public ImageForm()
        {
            InitializeComponent();
        }
        public IList<string> ImageList
        {
            get { return (IList<string>)this.imageListBox.DataSource; }
            set { this.imageListBox.DataSource = value; }
        }
        public int SelectedImage
        {
            get { return this.imageListBox.SelectedIndex; }
            set { this.imageListBox.SelectedIndex = value; }
        }
        public string Title
        {
            get { return this.titleTextBox.Text; }
            set { this.titleTextBox.Text = value; }
        }
        public string Tags
        {
            get { return this.tagsTextBox.Text; }
            set { this.tagsTextBox.Text = value; }
        }
        public presenter.presenter presenter
        { private get; set; }

        

        private void editBtn_Click(object sender, EventArgs e)
        {
            this.titleTextBox.ReadOnly = _isEditMode;
            this.tagsTextBox.ReadOnly = _isEditMode;

            _isEditMode = !_isEditMode;

            this.editBtn.Text = _isEditMode ? "Save" : "Edit";

            if(!_isEditMode)
            {
                presenter.UpdateImageView();
            }


        }

        private void imageListBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            presenter.UpdateImageView(imageListBox.SelectedIndex);
        }
    }
}
