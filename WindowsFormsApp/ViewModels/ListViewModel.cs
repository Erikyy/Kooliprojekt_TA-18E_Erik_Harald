using System.Collections.ObjectModel;
using System.Threading.Tasks;

namespace Wpf_App.ViewModels
{
    public class ListViewModel : NotifyPropertyChangedBase
    {
        private readonly HttpClient _httpClient = new HttpClient();
        private readonly IWindowService _windowService;



        public ObservableCollection<ListItem> Invoices { get; private set; }

        public RelayCommand<object> OpenNewInvoiceCommand { get; private set; }



        public ListViewModel() : this(new WindowService())

        {

        }

        public ListViewModel(IWindowService windowService)

        {
            _windowService = windowService;

            Invoices = new ObservableCollection<ListItem>();
            OpenNewInvoiceCommand = new RelayCommand<object>(arg =>

            {
                var result = _windowService.ShowDialog<AddInvoiceWindow>(null);
                if (!result)

                {
                    return;
                }
                Invoices.Clear();
                Load();
            });
            Load();

        }
        public async Task Load()

        {

            var invoices = await _httpClient.List(1);
            foreach (var invoice in invoices)

            {
                Invoices.Add(invoice);

            }

        }
    }
}
