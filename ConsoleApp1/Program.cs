using System;
using System.IO;


namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string finish_file = @"E:\Project_IRP\all.txt";
            string folderName = @"E:\Project_IRP\TRAINS"; //папка с текстовыми файлами
            string[] allFiles = Directory.GetFiles(folderName, "*.txt");
            string all2StringText = string.Empty;
            int numberOfStringInEachFile = 2;   //указываем номер строки, которую нужно считать
            foreach (string s in allFiles)
            {
                using (StreamReader sr = new StreamReader(new FileStream(s, FileMode.Open, FileAccess.Read)))
                {
                    for (int i = 0; i < numberOfStringInEachFile; i++)
                    {    //проскакиваем нужное количество строк
                        sr.ReadLine();
                    }
                    all2StringText += sr.ReadLine() + ";" + s.Substring(s.Length - 15, 11) + Environment.NewLine;

                }
            } 
            if (File.Exists("all.txt"))
            {
                File.Delete("all.txt");
            }
            
            File.WriteAllText( finish_file, all2StringText);  //сохранит в папку с исполняемым файлом. при необходимости прописать нужный путь
            Console.WriteLine("fifnished!");
            Console.ReadKey();
        }

    }
}
