using System.Windows;
using WindowsFormsApp.presenter;

namespace WindowsFormsApp.ViewModels
{
    public interface IWindowService
    {
        void ShowWindow<T>(object DataContext) where T : WindowService, new();

        bool ShowDialog<T>(object DataContext) where T : WindowService, new();

        
    }
    public class WindowService : IWindowService

    {

        public void ShowWindow<T>(object DataContext) where T : WindowService, new()

        {

            var window = new T();

            window.DataContext = DataContext;

            window.Show();

        }
        public bool ShowDialog<T>(object DataContext) where T : WindowService, new()

        {
            var window = new T();

            window.DataContext = DataContext;

            var result = window.ShowDialog();
            return (result.HasValue && result.Value);

        }
    }
}