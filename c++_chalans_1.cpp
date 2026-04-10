#include <iostream>

using namespace std;

void inputData (string names[], int scores[], int n) {
    //proses input nama dan skor tim (per each loops)
    for (int i = 0; i < 5; i++) {
        cout << "TIM " << i + 1 << endl;
        cout << "Masukkan nama tim: "; getline(cin >> ws, names[i]);
        cout << "Masukan skornya di sini: "; cin >> scores[i];
        cout << "\n===============\n";
    }
}

void bubbleSort (string names[], int scores[], int n) {
    //bagian bubble sort
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (scores[j] < scores[j+1]) {
                int temp_nilai = scores[j+1];
                scores[j+1] = scores[j];
                scores[j] = temp_nilai;

                string temp_nama = names[j+1];
                names[j+1] = names[j];
                names[j] = temp_nama;
            }
        }
    }
}

void showLeaderboard (string names[], int scores[], int n) {
    //print leaderboard onto screen
    cout << "Leaderboard: \n";
    for (int i = 0; i < 5; i++) {
        cout << i + 1 << ". " << names[i] << " - " << scores[i] << endl;
    }
}

int main() {
    string names[5];
    int scores[5];
    int n = 5; //(one-shot) untuk bubble sort karena maksimal element yg dapat ditampung adalah 5
    
    inputData(names, scores, 5);    
    bubbleSort(names, scores, 5);
    showLeaderboard(names, scores, 5);
}