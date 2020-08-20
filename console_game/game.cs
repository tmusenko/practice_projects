using System;

namespace ConsoleGame
{
    class Game : SuperGame
    {
        public new static void UpdatePosition(string keyPressed, out int x, out int y)
        {
            x = 0;
            y = 0;
            switch (keyPressed)
            {
                case "UpArrow":
                    y--;
                    break;
                case "DownArrow":
                    y++;
                    break;
                case "LeftArrow":
                    x--;
                    break;
                case "RightArrow":
                    x++;
                    break;
                case "W":
                    y--;
                    break;
                case "S":
                    y++;
                    break;
                case "A":
                    x--;
                    break;
                case "D":
                    x++;
                    break;
                default:
                    Console.WriteLine("Wrong key pressed...");
                    break;

            }
        }
        public new static char UpdateCursor(string keyPressed)
        {
            switch (keyPressed)
            {
                case "UpArrow":
                    return '^';
                    break;
                case "DownArrow":
                    return 'v';
                    break;
                case "LeftArrow":
                    return '<';
                    break;
                case "RightArrow":
                    return '>';
                    break;
                case "W":
                    return '^';
                    break;
                case "S":
                    return 'v';
                    break;
                case "A":
                    return '<';
                    break;
                case "D":
                    return '>';
                    break;
                default:
                    return '0';
                    break;
            }
        }
        public new static int KeepInBounds(int coord, int maxVal)
        {
            if (coord >= (maxVal - 1))
            {
                return 0;
            }
            else if (coord < 0)
            {
                return maxVal - 2;
            }
            else
            {
                return coord;
            }
        }
        public new static bool DidScore(int x, int y, int fruitX, int fruitY)
        {
            if (x == fruitX && y == fruitY)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
