#include <iostream>
#include <string>
#include <filesystem>
#include <cstdlib>

namespace fs = std::filesystem;

// Getting username
std::string get_username()
{
    for (const char *name : {"LOGNAME", "USER", "LNAME", "USERNAME"})
    {
        char *user = std::getenv(name);
        if (user)
        {
            return std::string(user);
        }
    }
    return "";
}

// Clearing temp files
void clear_tempfiles(const std::string &user)
{
    std::string path = "C:\\Users\\" + user + "\\AppData\\Local\\Temp";
    for (const auto &entry : fs::directory_iterator(path))
    {
        const std::string item_path = entry.path().string();
        try
        {
            if (fs::is_regular_file(entry))
            {
                fs::remove(entry);
            }
            else if (fs::is_directory(entry))
            {
                fs::remove_all(entry);
            }
            else
            {
                std::cout << "Skipped: " << item_path << " (Not a file or directory)\n";
            }
        }
        catch (const std::exception &e)
        {
            std::cerr << "Error deleting " << item_path << ": " << e.what() << "\n";
        }
    }
}

// Clearing prefetch
void clear_prefetch()
{
    std::string path = "C:\\Windows\\Prefetch";
    for (const auto &entry : fs::directory_iterator(path))
    {
        const std::string item_path = entry.path().string();
        try
        {
            if (fs::is_regular_file(entry))
            {
                fs::remove(entry);
            }
            else if (fs::is_directory(entry))
            {   
                std::cout << entry.path().string() << std::endl;
                fs::remove_all(entry);
            }
            else
            {
                std::cout << "Skipped: " << item_path << " (Not a file or directory)\n";
            }
        }
        catch (const std::exception &e)
        {
            std::cerr << "Error deleting " << item_path << ": " << e.what() << "\n";
        }
    }
}

// Clearing DNS cache
void clear_dns_cache()
{
    int result = std::system("ipconfig /flushdns");
    if (result == 0)
    {
        std::cout << "DNS cache flushed successfully." << std::endl;
    }
    else
    {
        std::cerr << "Error running ipconfig." << std::endl;
    }
}

int main()
{
    std::cout << "Just a second :), Hope you don't mind." << std::endl;
    std::string user = get_username();
    if (!user.empty())
    {
        clear_tempfiles(user);
        clear_prefetch();
        clear_dns_cache();
        std::cout << "Cleaned Successfully" << std::endl;
    }
    else
    {
        std::cerr << "Failed to retrieve the username." << std::endl;
    }
    return 0;
}
