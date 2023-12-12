
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}
        for path in paths:
            directory, *files = path.split()
            for file in files:
                file_name, content = file.split('(')
                content = content[:-1]  # Remove the closing parenthesis
                full_path = directory + '/' + file_name
                if content not in content_map:
                    content_map[content] = [full_path]
                else:
                    content_map[content].append(full_path)

        result = []
        for content, file_paths in content_map.items():
            if len(file_paths) > 1:
                result.append(file_paths)

        return result