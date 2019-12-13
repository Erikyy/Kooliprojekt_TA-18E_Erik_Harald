using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Input;

namespace Wpf_App.ViewModels
{
    public class RelayCommand<T> : ICommand

    {

        private readonly Action<T> _execute = null;

        private readonly Predicate<T> _canExecute = null;

        public RelayCommand(Action<T> execute) : this(execute, null)
        {

        }
        public RelayCommand(Action<T> execute, Predicate<T> canExecute)

        {

            if (execute == null)

            {

                throw new ArgumentNullException("execute");

            }

            _execute = execute;

            _canExecute = canExecute;

        }

        public bool CanExecute(object parameter)

        {
            return _canExecute == null ? true : _canExecute((T)parameter);
        }

        public event EventHandler CanExecuteChanged
        {
            add { CommandManager.RequerySuggested += value; }

            remove { CommandManager.RequerySuggested -= value; }

        }

        public void Execute(object parameter)

        {

            _execute((T)parameter);

        }

    }
}
