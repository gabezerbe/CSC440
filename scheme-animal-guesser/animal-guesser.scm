#lang racket

(struct animal (name attrs))

;a few attributes for our animals that the program will ask about
(define initial-attrs (list "mammal" "swimmer" "furry" "flyer" "digger" "blind" "brown" "red" "gray" "tail" "climber" "jumper" "tentacles"))

;define our animals

(define kangaroo (animal "Kangaroo" (list "mammal" "furry" "tail" "jumper")))
(define salmon(animal "Salmon" (list "swimmer" "red" "tail")))
(define whale(animal "Whale" (list "mammal" "swimmer" "gray" "tail")))
(define squid(animal "Squid" (list "swimmer" "gray" "tentacles")))
(define dog(animal "Dog" (list "mammal" "furry" "brown" "tail")))
(define mole(animal "Mole" (list "mammal" "digger" "furry" "brown" "blind")))
(define monkey(animal "Monkey" (list "mammal" "furry" "climber" "jumper" "brown" "tail")))

(define initial-animals (list kangaroo salmon dog mole monkey whale squid))

(define (filter-by-attr attr present animals)
  (filter (lambda (animal)
            (if present
                (member attr (animal-attrs animal))
                (not (member attr (animal-attrs animal)))))
          animals))

(define (get-all-attrs aval-animals)
  (set->list (list->set (foldr (lambda (animal acc) 
                                 (append (animal-attrs animal) acc)) 
                               null aval-animals))))

(define (add-animal all-animals asked)
  (printf "What is your animals name?\n")
  (let ([name (read)])
    (printf "What is an identifying characteristic?\n")
    (let* ([attr (format "~s" (read))]
          [new-animals (cons (animal name (cons attr asked)) all-animals)])
      (animal-loop new-animals
                   new-animals
                   (get-all-attrs new-animals)
                   null))))

(define (animal-loop all-animals current-animals current-attributes asked)
  (cond [(null? current-animals)
         (printf "I have no idea!\n")
         (add-animal all-animals asked)]
        [(null? (rest current-animals)) 
         (printf "I know! You're animal is the ~s\ny or n\n" 
                 (animal-name (first current-animals)))
         (let ([answer (read)])
           (if (not (equal? answer 'y))
               (add-animal all-animals asked)
               (begin (printf "I win! Let's play again\n") 
                      (animal-loop all-animals all-animals
                                   (get-all-attrs all-animals)
                                   null))))]
        [else (printf "~s?" (first current-attributes))
              (let ([answer (read)])
                (animal-loop all-animals
                             (filter-by-attr (first current-attributes)
                                             (equal? answer 'y)
                                             current-animals)
                             (rest current-attributes)
                             (if (equal? answer 'y) (cons (first current-attributes) asked) asked)))]))

(animal-loop initial-animals initial-animals (get-all-attrs initial-animals) null)