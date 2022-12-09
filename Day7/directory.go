package Day7

type DirectoryInterface interface {
	AddFile()
	AddChildDirectory()
}
type Directory struct {
	name string
	files []File
	childDirectories []Directory
}

func CreateDirectoy(name string) Directory {
	return Directory { name, []File{}, []Directory{} } 
}

func (cdir *Directory) AddFile(f File) {
	cdir.files = append(cdir.files, f)
}

func (cdir *Directory) AddChildDirectory(dir Directory) {
	cdir.childDirectories = append(cdir.childDirectories, dir)
}