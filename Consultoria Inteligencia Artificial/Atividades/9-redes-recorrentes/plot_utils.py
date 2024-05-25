import matplotlib.pyplot as plt
import numpy as np

def plot_1model_train_val_charts(history, save_path=''):
    """
    Plot training and validation loss and accuracy for one model
    """
    history_dict = history.history
    loss_values = history_dict['loss']
    val_loss_values = history_dict['val_loss']
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss_values, 'bo', label='Training loss')
    plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
    plt.xticks(epochs)
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.xticks(epochs)
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def pad_shorter_history(history, max_epochs):
    """Uses np.pad to add np.nan to shorter histories"""
    padded_history = {}
    for key, values in history.items():
        padded_history[key] = np.pad(values, (0, max_epochs - len(values)), mode='constant', constant_values=np.nan)
    return padded_history

# Funções de apoio
def plot_train_val_loss(*histories, history_labels: list=None, save_path=None, loss_labels=None, ylim=None):
    """Plots the training and validation loss from N histories"""
    np.random.seed(0)

    # Padding shorter history with np.nan to plot them together
    max_epochs = max([len(history.history['loss']) for history in histories])
    histories = [pad_shorter_history(history.history.copy(), max_epochs) for history in histories]

    # Create subplots
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))

    colors = plt.cm.rainbow(np.linspace(0, 1, len(histories)))
    np.random.shuffle(colors)

    for i, history in enumerate(histories):
        history_dict = history
        loss_values = history_dict['loss']
        val_loss_values = history_dict['val_loss']
        n_epochs = len(loss_values)

        best_epoch = np.nanargmin(val_loss_values)
        best_valid_loss = val_loss_values[best_epoch]
        epochs = range(1, len(loss_values) + 1)

        # Labels
        hist_label = history_labels[i] if history_labels else f"{i + 1}"
        best_model_stats = (f'Best Model {hist_label}\nepoch={best_epoch + 1}\n'
        f'loss={best_valid_loss:.2f}\nval_acc={history_dict["val_acc"][best_epoch]:.2f}')

        # Plotting loss lines
        ax.plot(epochs, loss_values, "--", linewidth=2, label=f"Training set {hist_label}", c=colors[i])
        ax.plot(epochs, val_loss_values, "-", linewidth=3, label=f"Validation set {hist_label}", c=colors[i])
        # Marking the best epoch
        ax.plot(best_epoch+1, best_valid_loss, "o", c=colors[i])
        ax.plot([0, n_epochs], [best_valid_loss, best_valid_loss], "k:", linewidth=2)
        ax.annotate(best_model_stats,
                    xy=(best_epoch+1, best_valid_loss),
                    xytext=(best_epoch+1, best_valid_loss + 0.04),
                    ha="center",
                    arrowprops=dict(facecolor='black', shrink=0.05))

    ax.grid()
    ax.set_title('Training and validation loss')
    ax.set_xlabel('Epochs')
    ax.set_ylabel(f'{loss_labels[i] if loss_labels else "Categorical Crossentropy"} loss')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # ax.axis([0, n_epochs, 0, 0.10])
    plt.tight_layout()
    if ylim:
        plt.ylim(ylim)
    if save_path:
        plt.savefig(save_path)

def plot_train_val_charts(history1, history2, model_1_label='1', model_2_label='2', save_path='', color_1='b', color_2='r'):
    """
    Compare two models training and validation loss and accuracy
    """
    history_dict1 = history1.history
    history_dict2 = history2.history
    loss_values1 = history_dict1['loss']
    val_loss_values1 = history_dict1['val_loss']
    loss_values2 = history_dict2['loss']
    val_loss_values2 = history_dict2['val_loss']
    acc1 = history1.history['acc']
    acc2 = history2.history['acc']
    val_acc1 = history1.history['val_acc']
    val_acc2 = history2.history['val_acc']
    epochs = range(1, len(acc1) + 1)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss_values1, f'{color_1}o', label=f'Training loss Model {model_1_label}')
    plt.plot(epochs, val_loss_values1, color_1, label=f'Validation loss Model {model_1_label}')
    plt.plot(epochs, loss_values2, f'{color_2}o', label=f'Training loss Model {model_2_label}')
    plt.plot(epochs, val_loss_values2, color_2, label=f'Validation loss Model {model_2_label}')
    plt.xticks(epochs)
    plt.title(f'Training and validation loss Model {model_1_label} vs Model {model_2_label}')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(epochs, acc1, f'{color_1}o', label=f'Training acc Model {model_1_label}')
    plt.plot(epochs, val_acc1, color_1, label=f'Validation acc Model {model_1_label}')
    plt.plot(epochs, acc2, f'{color_2}o', label=f'Training acc Model {model_2_label}')
    plt.plot(epochs, val_acc2, color_2, label=f'Validation acc Model {model_2_label}')
    plt.xticks(epochs)
    plt.title(f'Training and validation accuracy Model {model_1_label} vs Model {model_2_label}')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()