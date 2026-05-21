# 如何解决webview每次调试都需要寻找进程号问题

**问题背景：**



在应用开发过程中，调试Web页面时，每次启动DevTools都需要重新映射端口。



**解决方案：**



参考以下示例代码，文件内容编写完成后，将文件扩展名更改为.bat。每次调试后，运行bat文件以自动获取进程号。



```cangjie
1. // xxx.bat
2. @echo off
3. setlocal
4.
5. :: Set devtools parameter
6. hdc shell param set web.debug.devtools true
7. if errorlevel 1 (
8.  echo Error: Failed to set devtools parameter.
9.  pause
10.  exit /b
11. )
12.
13. :: Get the domain socket name of devtools
14. for /f "tokens=*" %%a in ('hdc shell "cat /proc/net/unix | grep devtools"') do set SOCKET_NAME=%%a
15. if not defined SOCKET_NAME (
16.  echo Error: Failed to get the domain socket name of devtools.
17.  pause
18.  exit /b
19. )
20.
21. :: Extract process ID
22. // tokens=4 indicates extracting the field separated by the fourth underscore as the PID
23. for /f "delims=_ tokens=4" %%a in ("%SOCKET_NAME%") do set PID=%%a
24. if not defined PID (
25.  echo Error: Failed to extract process ID.
26.  pause
27.  exit /b
28. )
29.
30. :: Add mapping
31. hdc fport tcp:9222 localabstract:webview_devtools_remote_%PID%
32. if errorlevel 1 (
33.  echo Error: Failed to add mapping.
34.  pause
35.  exit /b
36. )
37.
38. :: Check mapping
39. hdc fport ls
40.
41. echo.
42. echo Script executed successfully. Press any key to exit...
43. pause >nul
44.
45. :: Try opening the page in Edge
46. start msedge chrome://inspect/#devices.com
47.
48. :: If Edge is unavailable, open the page in Chrome
49. if errorlevel 1 (
50.  start chrome chrome://inspect/#devices.com
51. )
52.
53. endlocal

```


[DebugProcessId.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/DebugProcessId.txt#L6-L58)
