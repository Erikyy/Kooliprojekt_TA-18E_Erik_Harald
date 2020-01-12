using System.Collections.ObjectModel;
using System.Threading.Tasks;
using System.Windows.Documents;
using WindowsFormsApp.forms;
using WindowsFormsApp.HttpClient;

namespace WindowsFormsApp.ViewModels
{
    public class ListViewModel : NotifyPropertyChangedBase
    {
        private readonly Client _httpClient = new Client();
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
                var result = _windowService.ShowDialog<ImageForm>(null);
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
