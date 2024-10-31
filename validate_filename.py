import re

def validate(input_str, show=False):
    # remove illegal characters for Windows file names/paths
    # (illegal filenames are a superset (41) of the illegal path names (36))
    # this is according to windows blacklist obtained with Powershell
    # from: https://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names/44750843#44750843
    #
    # PS> $enc = [system.Text.Encoding]::UTF8
    # PS> $FileNameInvalidChars = [System.IO.Path]::GetInvalidFileNameChars()
    # PS> $FileNameInvalidChars | foreach { $enc.GetBytes($_) } | Out-File -FilePath InvalidFileCharCodes.txt

    illegal = '\u0022\u003c\u003e\u007c\u0000\u0001\u0002\u0003\u0004\u0005\u0006\u0007\u0008' + \
              '\u0009\u000a\u000b\u000c\u000d\u000e\u000f\u0010\u0011\u0012\u0013\u0014\u0015' + \
              '\u0016\u0017\u0018\u0019\u001a\u001b\u001c\u001d\u001e\u001f\u003a\u002a\u003f\u005c\u002f'

    output_str, _ = re.subn('['+illegal+']','_', input_str)
    output_str = output_str.replace('\\','_')   # backslash cannot be handled by regex
    output_str = output_str.replace('..','_')   # double dots are illegal too, or at least a bad idea
    output_str = output_str[:-1] if output_str[-1] == '.' else output_str # can't have end of line '.'

    if show and output_str != input_str:
        print(f"The name '{input_str}' had invalid characters, "
              f"name was modified to '{output_str}'")

    return output_str

if __name__ == '__main__':
    validate('588370 *namirin - Songs Compilation.osz', True)
